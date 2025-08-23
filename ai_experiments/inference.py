import torch
import torch.nn.functional as F
import argparse
import logging
import time
import numpy as np
from tqdm import tqdm
import os
from transformer import Transformer, vocab, tokenize, detokenize

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('inference.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class BeamSearchNode:
    def __init__(self, hidden_state, prev_node, token_id, log_prob, length):
        self.hidden_state = hidden_state
        self.prev_node = prev_node
        self.token_id = token_id
        self.log_prob = log_prob
        self.length = length

    def eval(self, alpha=1.0):
        # Length normalization to avoid bias toward shorter sequences
        return self.log_prob / (self.length ** alpha)


def top_k_top_p_filtering(logits, top_k=0, top_p=0.0, filter_value=-float('Inf')):
    """Filter a distribution of logits using top-k and/or nucleus (top-p) filtering"""
    top_k = min(top_k, logits.size(-1))  # Safety check

    if top_k > 0:
        # Remove all tokens with a probability less than the last token of the top-k
        indices_to_remove = logits < torch.topk(logits, top_k)[
            0][..., -1, None]
        logits[indices_to_remove] = filter_value

    if top_p > 0.0:
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(
            F.softmax(sorted_logits, dim=-1), dim=-1)

        # Remove tokens with cumulative probability above the threshold
        sorted_indices_to_remove = cumulative_probs > top_p
        # Shift the indices to the right to keep also the first token above the threshold
        sorted_indices_to_remove[...,
                                 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0

        indices_to_remove = sorted_indices[sorted_indices_to_remove]
        logits[indices_to_remove] = filter_value

    return logits


def generate_text_greedy(model, src_ids, max_length=20, start_token='<s>', end_token='</s>'):
    """Generate text using greedy decoding"""
    device = next(model.parameters()).device
    model.eval()

    # Prepare source tensor
    src_tensor = torch.tensor([src_ids], dtype=torch.long, device=device)
    src_pad_mask = (src_tensor == vocab['<pad>']).unsqueeze(1).unsqueeze(2)

    with torch.no_grad():
        # Encode source sequence
        src_embedded = model.positional_encoding(model.src_embed(src_tensor))
        encoder_output = model.encoder(src_embedded, src_mask=src_pad_mask)

    # Start the target sequence with the start token
    tgt_ids = [vocab[start_token]]

    for _ in range(max_length):
        tgt_tensor = torch.tensor([tgt_ids], dtype=torch.long, device=device)

        # Create target mask for self-attention
        tgt_len = tgt_tensor.size(1)
        tgt_sub_mask = torch.triu(torch.ones(
            (tgt_len, tgt_len), device=device) == 1).transpose(0, 1)
        tgt_sub_mask = tgt_sub_mask.float().masked_fill(tgt_sub_mask == 0, float('-inf')
                                                        ).masked_fill(tgt_sub_mask == 1, float(0.0))

        with torch.no_grad():
            # Decode target sequence
            tgt_embedded = model.positional_encoding(
                model.tgt_embed(tgt_tensor))
            decoder_output = model.decoder(
                tgt_embedded,
                encoder_output,
                src_mask=src_pad_mask,
                tgt_mask=tgt_sub_mask
            )
            logits = model.output_linear(decoder_output)

        # Greedy decoding: choose token with highest probability
        next_token_logits = logits[0, -1, :]
        next_token_id = torch.argmax(next_token_logits).item()
        tgt_ids.append(next_token_id)

        if next_token_id == vocab[end_token]:
            break

    # Exclude the start token when detokenizing the output
    return detokenize(tgt_ids[1:])


def generate_text_sampling(model, src_ids, max_length=20, start_token='<s>', end_token='</s>',
                           temperature=1.0, top_k=0, top_p=0.9):
    """Generate text using sampling with temperature, top-k, and top-p filtering"""
    device = next(model.parameters()).device
    model.eval()

    # Prepare source tensor
    src_tensor = torch.tensor([src_ids], dtype=torch.long, device=device)
    src_pad_mask = (src_tensor == vocab['<pad>']).unsqueeze(1).unsqueeze(2)

    with torch.no_grad():
        # Encode source sequence
        src_embedded = model.positional_encoding(model.src_embed(src_tensor))
        encoder_output = model.encoder(src_embedded, src_mask=src_pad_mask)

    # Start the target sequence with the start token
    tgt_ids = [vocab[start_token]]

    for _ in range(max_length):
        tgt_tensor = torch.tensor([tgt_ids], dtype=torch.long, device=device)

        # Create target mask for self-attention
        tgt_len = tgt_tensor.size(1)
        tgt_sub_mask = torch.triu(torch.ones(
            (tgt_len, tgt_len), device=device) == 1).transpose(0, 1)
        tgt_sub_mask = tgt_sub_mask.float().masked_fill(tgt_sub_mask == 0, float('-inf')
                                                        ).masked_fill(tgt_sub_mask == 1, float(0.0))

        with torch.no_grad():
            # Decode target sequence
            tgt_embedded = model.positional_encoding(
                model.tgt_embed(tgt_tensor))
            decoder_output = model.decoder(
                tgt_embedded,
                encoder_output,
                src_mask=src_pad_mask,
                tgt_mask=tgt_sub_mask
            )
            logits = model.output_linear(decoder_output)

        # Get logits for the next token
        next_token_logits = logits[0, -1, :] / temperature

        # Apply filtering
        filtered_logits = top_k_top_p_filtering(
            next_token_logits, top_k=top_k, top_p=top_p)

        # Sample from the filtered distribution
        probs = F.softmax(filtered_logits, dim=-1)
        next_token_id = torch.multinomial(probs, 1).item()

        tgt_ids.append(next_token_id)

        if next_token_id == vocab[end_token]:
            break

    # Exclude the start token when detokenizing the output
    return detokenize(tgt_ids[1:])


def generate_text_beam_search(model, src_ids, max_length=20, start_token='<s>', end_token='</s>',
                              beam_width=5, alpha=0.7):
    """Generate text using beam search"""
    device = next(model.parameters()).device
    model.eval()

    # Prepare source tensor and mask
    src_tensor = torch.tensor([src_ids], dtype=torch.long, device=device)
    src_pad_mask = (src_tensor == vocab['<pad>']).unsqueeze(1).unsqueeze(2)

    with torch.no_grad():
        # Encode source sequence
        src_embedded = model.positional_encoding(model.src_embed(src_tensor))
        encoder_output = model.encoder(src_embedded, src_mask=src_pad_mask)

    # Start the target sequence with the start token
    start_token_id = vocab[start_token]
    end_token_id = vocab[end_token]

    # Initialize beam with just the start token
    tgt_tensor = torch.tensor(
        [[start_token_id]], dtype=torch.long, device=device)

    # Create initial node
    with torch.no_grad():
        # Get initial decoder output for the start token
        tgt_embedded = model.positional_encoding(model.tgt_embed(tgt_tensor))
        tgt_mask = torch.zeros((1, 1), device=device).bool()
        decoder_output = model.decoder(
            tgt_embedded,
            encoder_output,
            src_mask=src_pad_mask,
            tgt_mask=tgt_mask
        )
        logits = model.output_linear(decoder_output)
        probs = F.log_softmax(logits, dim=-1)

    # Initialize beam
    top_k_probs, top_k_idx = probs[0, -1, :].topk(beam_width)
    beam_nodes = []

    # Create initial beam nodes
    for prob, idx in zip(top_k_probs, top_k_idx):
        beam_nodes.append(BeamSearchNode(
            hidden_state=decoder_output,  # Reuse for simplicity
            prev_node=None,
            token_id=idx.item(),
            log_prob=prob.item(),
            length=1
        ))

    # Track completed sequences
    endnodes = []

    # Beam search loop
    for step in range(max_length - 1):
        # Break if we've found enough end nodes
        if len(endnodes) >= beam_width:
            break

        # Get candidate nodes for this step
        candidates = []

        # Expand each node in the beam
        for beam_node in beam_nodes:
            # Skip if this node already generated an EOS
            if beam_node.token_id == end_token_id:
                endnodes.append(beam_node)
                continue

            # Create the sequence so far
            seq = []
            node = beam_node
            while node:
                if node.prev_node:  # Skip the start node
                    seq.append(node.token_id)
                node = node.prev_node
            seq.reverse()
            seq = [start_token_id] + seq

            # Convert sequence to tensor
            tgt_tensor = torch.tensor([seq], dtype=torch.long, device=device)

            # Create target mask
            tgt_len = tgt_tensor.size(1)
            tgt_sub_mask = torch.triu(torch.ones(
                (tgt_len, tgt_len), device=device) == 1).transpose(0, 1)
            tgt_sub_mask = tgt_sub_mask.float().masked_fill(tgt_sub_mask == 0, float('-inf')
                                                            ).masked_fill(tgt_sub_mask == 1, float(0.0))

            with torch.no_grad():
                # Decode
                tgt_embedded = model.positional_encoding(
                    model.tgt_embed(tgt_tensor))
                decoder_output = model.decoder(
                    tgt_embedded,
                    encoder_output,
                    src_mask=src_pad_mask,
                    tgt_mask=tgt_sub_mask
                )
                logits = model.output_linear(decoder_output)
                probs = F.log_softmax(logits, dim=-1)

            # Get top-k candidates for the next token
            top_k_probs, top_k_idx = probs[0, -1, :].topk(beam_width)

            # Create new nodes for each candidate
            for prob, idx in zip(top_k_probs, top_k_idx):
                candidates.append(BeamSearchNode(
                    hidden_state=decoder_output,
                    prev_node=beam_node,
                    token_id=idx.item(),
                    log_prob=beam_node.log_prob + prob.item(),
                    length=beam_node.length + 1
                ))

        # No candidates? Break
        if not candidates:
            break

        # Select the beam_width best candidates
        candidates.sort(key=lambda node: -node.eval(alpha))
        beam_nodes = candidates[:beam_width]

    # If we didn't find enough end nodes, add the best incomplete ones
    if len(endnodes) < beam_width:
        endnodes.extend(beam_nodes[:beam_width - len(endnodes)])

    # Select the best end node
    endnodes.sort(key=lambda node: -node.eval(alpha))
    best_node = endnodes[0]

    # Reconstruct the sequence
    seq = []
    node = best_node
    while node and node.prev_node:  # Skip the start node
        seq.append(node.token_id)
        node = node.prev_node
    seq.reverse()

    # Detokenize
    return detokenize(seq)


def batch_inference(model, input_file, output_file, method='greedy', batch_size=32, **kwargs):
    """Run inference on a batch of inputs from a file"""
    device = next(model.parameters()).device
    model.eval()

    # Load inputs
    inputs = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            inputs.append(line.strip())

    # Configure generation method
    if method == 'greedy':
        def generate_fn(x): return generate_text_greedy(model, x, **kwargs)
    elif method == 'sampling':
        def generate_fn(x): return generate_text_sampling(model, x, **kwargs)
    elif method == 'beam_search':
        def generate_fn(x): return generate_text_beam_search(
            model, x, **kwargs)
    else:
        raise ValueError(f"Unknown generation method: {method}")

    # Process in batches
    outputs = []
    with tqdm(total=len(inputs), desc=f"Running {method} inference") as pbar:
        for i in range(0, len(inputs), batch_size):
            batch = inputs[i:i+batch_size]
            batch_outputs = []

            for input_text in batch:
                src_ids = tokenize(input_text)
                if not src_ids:
                    batch_outputs.append("")
                else:
                    output_text = generate_fn(src_ids)
                    batch_outputs.append(output_text)

            outputs.extend(batch_outputs)
            pbar.update(len(batch))

    # Save outputs
    with open(output_file, 'w', encoding='utf-8') as f:
        for output in outputs:
            f.write(f"{output}\n")

    logger.info(f"Saved {len(outputs)} outputs to {output_file}")


def interactive_mode(model, method='greedy', **kwargs):
    """Interactive mode for generation"""
    logger.info(f"Interactive mode using {method} generation")
    logger.info("Enter input text (type 'quit' to exit):")

    # Configure generation method
    if method == 'greedy':
        def generate_fn(x): return generate_text_greedy(model, x, **kwargs)
    elif method == 'sampling':
        def generate_fn(x): return generate_text_sampling(model, x, **kwargs)
    elif method == 'beam_search':
        def generate_fn(x): return generate_text_beam_search(
            model, x, **kwargs)
    else:
        raise ValueError(f"Unknown generation method: {method}")

    while True:
        try:
            input_text = input("> ").strip()
            if input_text.lower() in ['quit', 'exit', 'q']:
                break

            start_time = time.time()
            src_ids = tokenize(input_text)

            if not src_ids:
                print("No valid tokens found. Please try again.")
                continue

            output_text = generate_fn(src_ids)
            elapsed = time.time() - start_time

            print(f"Generated ({elapsed:.2f}s): {output_text}")

        except KeyboardInterrupt:
            print("\nStopping interactive mode.")
            break
        except Exception as e:
            logger.error(f"Error during generation: {e}")
            print(f"An error occurred: {e}")


def load_model(model_path, config=None):
    """Load trained model with proper error handling"""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    if config is None:
        # Default configuration
        config = {
            'd_model': 128,
            'n_heads': 4,
            'num_layers': 2,
            'd_ff': 512,
            'dropout': 0.1,
            'max_len': 20
        }

    model = Transformer(
        src_vocab_size=len(vocab),
        tgt_vocab_size=len(vocab),
        num_layers=config['num_layers'],
        d_model=config['d_model'],
        n_heads=config['n_heads'],
        d_ff=config['d_ff'],
        dropout=config['dropout'],
        max_len=config['max_len']
    ).to(device)

    try:
        # Try to load as state dict
        checkpoint = torch.load(model_path, map_location=device)

        # Check if it's a checkpoint or just state dict
        if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'])
            logger.info(
                f"Loaded model from checkpoint at epoch {checkpoint.get('epoch', 'unknown')}")
        else:
            model.load_state_dict(checkpoint)
            logger.info(f"Loaded model state dict from {model_path}")

    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

    model.eval()
    return model


def main():
    parser = argparse.ArgumentParser(description="Transformer Inference")
    parser.add_argument('--model', type=str, default='trained_transformer.pt',
                        help='Path to the trained model')
    parser.add_argument('--mode', type=str, choices=['interactive', 'batch'], default='interactive',
                        help='Inference mode: interactive or batch')
    parser.add_argument('--method', type=str, choices=['greedy', 'sampling', 'beam_search'],
                        default='greedy', help='Text generation method')
    parser.add_argument('--max_length', type=int, default=20,
                        help='Maximum generation length')
    parser.add_argument('--temperature', type=float, default=1.0,
                        help='Sampling temperature (higher = more random)')
    parser.add_argument('--top_k', type=int, default=0,
                        help='Top-k filtering (0 = disabled)')
    parser.add_argument('--top_p', type=float, default=0.9,
                        help='Nucleus sampling probability threshold')
    parser.add_argument('--beam_width', type=int, default=5,
                        help='Beam search width')
    parser.add_argument('--alpha', type=float, default=0.7,
                        help='Length penalty for beam search')
    parser.add_argument('--input_file', type=str, default=None,
                        help='Input file for batch mode')
    parser.add_argument('--output_file', type=str, default='outputs.txt',
                        help='Output file for batch mode')
    parser.add_argument('--batch_size', type=int, default=32,
                        help='Batch size for batch mode')
    parser.add_argument('--checkpoint_dir', type=str, default='checkpoints',
                        help='Checkpoint directory to load the best model')
    parser.add_argument('--use_best', action='store_true',
                        help='Use the best checkpoint instead of the specified model')

    args = parser.parse_args()

    # Determine model path
    model_path = args.model
    if args.use_best:
        best_checkpoint = os.path.join(
            args.checkpoint_dir, 'best_checkpoint.pt')
        if os.path.exists(best_checkpoint):
            model_path = best_checkpoint
            logger.info(f"Using best checkpoint: {best_checkpoint}")
        else:
            logger.warning(
                f"Best checkpoint not found at {best_checkpoint}, using {model_path} instead")

    # Load model
    model = load_model(model_path)

    # Prepare generation kwargs
    kwargs = {
        'max_length': args.max_length,
        'start_token': '<s>',
        'end_token': '</s>'
    }

    if args.method == 'sampling':
        kwargs.update({
            'temperature': args.temperature,
            'top_k': args.top_k,
            'top_p': args.top_p
        })
    elif args.method == 'beam_search':
        kwargs.update({
            'beam_width': args.beam_width,
            'alpha': args.alpha
        })

    # Run inference
    if args.mode == 'interactive':
        interactive_mode(model, method=args.method, **kwargs)
    else:  # batch mode
        if not args.input_file:
            logger.error("Input file is required for batch mode")
            return
        batch_inference(
            model, args.input_file, args.output_file,
            method=args.method, batch_size=args.batch_size, **kwargs
        )


if __name__ == '__main__':
    main()
