import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
from torch.optim.lr_scheduler import ReduceLROnPlateau
from transformer import Transformer, vocab, tokenize
import time
import logging
import argparse
from tqdm import tqdm
import os
import numpy as np
import matplotlib.pyplot as plt
import random

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('training.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Set seeds for reproducibility


def set_seed(seed=42):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True

# ------------------------------
# Dataset and Dataloader
# ------------------------------


class ReverseDataset(Dataset):
    def __init__(self, filepath, max_len=20):
        self.samples = []
        self.max_len = max_len

        try:
            with open(filepath, 'r') as f:
                for line in f:
                    if '\t' in line:
                        src, tgt = line.strip().split('\t')
                        self.samples.append((src, tgt))
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            raise

        logger.info(f"Loaded {len(self.samples)} samples from {filepath}")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        src_text, tgt_text = self.samples[idx]
        src_ids = tokenize(src_text)[:self.max_len]
        tgt_ids = tokenize(tgt_text)[:self.max_len]

        # Add <s> and </s> tokens
        tgt_input = [vocab['<s>']] + tgt_ids
        tgt_output = tgt_ids + [vocab['</s>']]

        # Pad to max_len
        src_ids += [vocab['<pad>']] * (self.max_len - len(src_ids))
        tgt_input += [vocab['<pad>']] * \
            (self.max_len + 1 - len(tgt_input))  # +1 for <s>
        tgt_output += [vocab['<pad>']] * \
            (self.max_len + 1 - len(tgt_output))  # +1 for </s>

        return {
            'src': torch.tensor(src_ids, dtype=torch.long),
            'tgt_input': torch.tensor(tgt_input, dtype=torch.long),
            'tgt_output': torch.tensor(tgt_output, dtype=torch.long),
            'src_len': len(src_text),
            'tgt_len': len(tgt_text)
        }


def create_masks(src, tgt_input):
    # Source padding mask
    src_pad_mask = (src == vocab['<pad>']).unsqueeze(
        1).unsqueeze(2)  # (batch, 1, 1, src_len)

    # Target padding mask
    tgt_pad_mask = (tgt_input == vocab['<pad>']).unsqueeze(
        1).unsqueeze(2)  # (batch, 1, 1, tgt_len)

    # Target subsequent mask (for autoregressive property)
    tgt_len = tgt_input.size(1)
    tgt_sub_mask = torch.triu(torch.ones(
        (tgt_len, tgt_len), device=src.device) == 1).transpose(0, 1)
    tgt_sub_mask = tgt_sub_mask.float().masked_fill(tgt_sub_mask == 0, float('-inf')
                                                    ).masked_fill(tgt_sub_mask == 1, float(0.0))

    # Combine target masks
    tgt_mask = tgt_pad_mask | tgt_sub_mask.unsqueeze(0)

    return src_pad_mask, tgt_mask

# ------------------------------
# Training and Evaluation Functions
# ------------------------------


def train_epoch(model, dataloader, optimizer, criterion, device, scheduler=None, clip_grad=1.0):
    model.train()
    total_loss = 0
    start_time = time.time()

    for batch in tqdm(dataloader, desc="Training"):
        src = batch['src'].to(device)
        tgt_input = batch['tgt_input'].to(device)
        tgt_output = batch['tgt_output'].to(device)

        src_pad_mask, tgt_mask = create_masks(src, tgt_input)

        optimizer.zero_grad()

        output = model(src, tgt_input, src_mask=src_pad_mask,
                       tgt_mask=tgt_mask)

        # Reshape for loss calculation
        output = output.contiguous().view(-1, output.size(-1))
        tgt_output = tgt_output.contiguous().view(-1)

        loss = criterion(output, tgt_output)
        loss.backward()

        # Gradient clipping
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip_grad)

        optimizer.step()
        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    elapsed_time = time.time() - start_time

    if scheduler:
        scheduler.step(avg_loss)

    return avg_loss, elapsed_time


def evaluate(model, dataloader, criterion, device):
    model.eval()
    total_loss = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Evaluating"):
            src = batch['src'].to(device)
            tgt_input = batch['tgt_input'].to(device)
            tgt_output = batch['tgt_output'].to(device)

            src_pad_mask, tgt_mask = create_masks(src, tgt_input)

            output = model(src, tgt_input, src_mask=src_pad_mask,
                           tgt_mask=tgt_mask)

            # Reshape for loss calculation
            output = output.contiguous().view(-1, output.size(-1))
            tgt_output = tgt_output.contiguous().view(-1)

            loss = criterion(output, tgt_output)
            total_loss += loss.item()

    return total_loss / len(dataloader)


def save_checkpoint(model, optimizer, scheduler, epoch, loss, filepath):
    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict() if scheduler else None,
        'loss': loss
    }
    torch.save(checkpoint, filepath)
    logger.info(f"Checkpoint saved to {filepath}")


def load_checkpoint(model, optimizer, scheduler, filepath, device):
    if not os.path.exists(filepath):
        logger.warning(f"No checkpoint found at {filepath}")
        return 0, float('inf')

    checkpoint = torch.load(filepath, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    if scheduler and checkpoint['scheduler_state_dict']:
        scheduler.load_state_dict(checkpoint['scheduler_state_dict'])

    logger.info(f"Loaded checkpoint from epoch {checkpoint['epoch']}")
    return checkpoint['epoch'], checkpoint['loss']


def plot_losses(train_losses, val_losses, save_path='loss_plot.png'):
    plt.figure(figsize=(10, 6))
    plt.plot(train_losses, label='Training Loss')
    plt.plot(val_losses, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    logger.info(f"Loss plot saved to {save_path}")

# ------------------------------
# Main
# ------------------------------


def main():
    parser = argparse.ArgumentParser(description='Train a Transformer model')
    parser.add_argument('--train_file', type=str,
                        default='data.txt', help='Training data file')
    parser.add_argument('--val_file', type=str, default=None,
                        help='Validation data file')
    parser.add_argument('--val_split', type=float, default=0.1,
                        help='Validation split if no validation file')
    parser.add_argument('--d_model', type=int, default=128,
                        help='Model dimension')
    parser.add_argument('--n_heads', type=int, default=4,
                        help='Number of attention heads')
    parser.add_argument('--num_layers', type=int, default=2,
                        help='Number of encoder/decoder layers')
    parser.add_argument('--d_ff', type=int, default=512,
                        help='Feed forward dimension')
    parser.add_argument('--dropout', type=float,
                        default=0.1, help='Dropout rate')
    parser.add_argument('--max_len', type=int, default=20,
                        help='Maximum sequence length')
    parser.add_argument('--batch_size', type=int,
                        default=32, help='Batch size')
    parser.add_argument('--num_epochs', type=int,
                        default=10, help='Number of epochs')
    parser.add_argument('--learning_rate', type=float,
                        default=1e-3, help='Learning rate')
    parser.add_argument('--clip_grad', type=float,
                        default=1.0, help='Gradient clipping')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--checkpoint_dir', type=str,
                        default='checkpoints', help='Checkpoint directory')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from checkpoint')

    args = parser.parse_args()

    # Set seeds for reproducibility
    set_seed(args.seed)

    # Setup device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logger.info(f"Using device: {device}")

    # Create checkpoint directory
    os.makedirs(args.checkpoint_dir, exist_ok=True)

    # Load and split dataset
    if args.val_file:
        train_dataset = ReverseDataset(args.train_file, args.max_len)
        val_dataset = ReverseDataset(args.val_file, args.max_len)
    else:
        full_dataset = ReverseDataset(args.train_file, args.max_len)
        val_size = int(len(full_dataset) * args.val_split)
        train_size = len(full_dataset) - val_size
        train_dataset, val_dataset = torch.utils.data.random_split(
            full_dataset, [train_size, val_size])
        logger.info(
            f"Split dataset: {train_size} training samples, {val_size} validation samples")

    train_dataloader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=4,
        pin_memory=True if torch.cuda.is_available() else False
    )

    val_dataloader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=4,
        pin_memory=True if torch.cuda.is_available() else False
    )

    # Initialize model
    model = Transformer(
        src_vocab_size=len(vocab),
        tgt_vocab_size=len(vocab),
        num_layers=args.num_layers,
        d_model=args.d_model,
        n_heads=args.n_heads,
        d_ff=args.d_ff,
        dropout=args.dropout,
        max_len=args.max_len
    ).to(device)

    logger.info(
        f"Model has {sum(p.numel() for p in model.parameters() if p.requires_grad):,} trainable parameters")

    # Initialize optimizer, scheduler, and loss function
    optimizer = optim.Adam(
        model.parameters(), lr=args.learning_rate, betas=(0.9, 0.98), eps=1e-9)
    scheduler = ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=2, verbose=True)
    criterion = nn.CrossEntropyLoss(ignore_index=vocab['<pad>'])

    # Resume from checkpoint if requested
    start_epoch = 0
    best_val_loss = float('inf')
    train_losses = []
    val_losses = []

    if args.resume:
        checkpoint_path = os.path.join(
            args.checkpoint_dir, 'latest_checkpoint.pt')
        start_epoch, best_val_loss = load_checkpoint(
            model, optimizer, scheduler, checkpoint_path, device)

    # Training loop
    logger.info("Starting training...")

    for epoch in range(start_epoch, args.num_epochs):
        train_loss, train_time = train_epoch(
            model, train_dataloader, optimizer, criterion, device, scheduler, args.clip_grad
        )
        train_losses.append(train_loss)

        val_loss = evaluate(model, val_dataloader, criterion, device)
        val_losses.append(val_loss)

        logger.info(f"Epoch {epoch+1}/{args.num_epochs} | "
                    f"Train Loss: {train_loss:.4f} | "
                    f"Val Loss: {val_loss:.4f} | "
                    f"Time: {train_time:.2f}s | "
                    f"LR: {optimizer.param_groups[0]['lr']:.6f}")

        # Save checkpoint
        save_checkpoint(
            model, optimizer, scheduler, epoch + 1, val_loss,
            os.path.join(args.checkpoint_dir, 'latest_checkpoint.pt')
        )

        # Save best model
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            save_checkpoint(
                model, optimizer, scheduler, epoch + 1, val_loss,
                os.path.join(args.checkpoint_dir, 'best_checkpoint.pt')
            )
            logger.info(f"New best validation loss: {best_val_loss:.4f}")

    # Plot losses
    plot_losses(train_losses, val_losses)

    # Save final model
    torch.save(model.state_dict(), 'trained_transformer.pt')
    logger.info("Final model saved to trained_transformer.pt")


if __name__ == '__main__':
    main()
