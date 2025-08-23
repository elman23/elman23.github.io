import math
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Dict, List, Tuple, Union
import numpy as np


class PositionalEncoding(nn.Module):
    """Positional encoding for the transformer model."""

    def __init__(self, d_model: int, max_len: int = 5000, dropout: float = 0.1):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Create positional encoding matrix
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(
            0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        # Apply sine to even indices and cosine to odd indices
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)  # (1, max_len, d_model)

        # Register buffer to allow saving and loading with the model
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Tensor of shape [batch_size, seq_len, d_model]
        Returns:
            Output tensor with added positional encoding
        """
        x = x + self.pe[:, :x.size(1)]
        return self.dropout(x)


class MultiHeadAttention(nn.Module):
    """Multi-head attention mechanism."""

    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.1):
        super().__init__()
        assert d_model % n_heads == 0, "d_model must be divisible by n_heads"

        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        # Linear projections for Q, K, V and output
        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

        # For storing attention weights if needed
        self.attention_weights = None

    def forward(self,
                query: torch.Tensor,
                key: torch.Tensor,
                value: torch.Tensor,
                mask: Optional[torch.Tensor] = None,
                return_attention: bool = False) -> Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]:
        """
        Args:
            query: Query tensor [batch_size, seq_len_q, d_model]
            key: Key tensor [batch_size, seq_len_k, d_model]
            value: Value tensor [batch_size, seq_len_v, d_model]
            mask: Optional mask tensor
            return_attention: Whether to return attention weights

        Returns:
            Output tensor and optionally attention weights
        """
        batch_size = query.size(0)

        # Linear projections and reshape for multi-head attention
        q = self.q_proj(query).view(
            batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        k = self.k_proj(key).view(
            batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        v = self.v_proj(value).view(
            batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        # Compute attention scores
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)

        # Apply mask if provided
        if mask is not None:
            # Expand mask for multi-head attention if needed
            # [batch, seq_len_q, seq_len_k] -> [batch, heads, seq_len_q, seq_len_k]
            if mask.dim() == 3 and scores.dim() == 4:
                mask = mask.unsqueeze(1)
            scores = scores.masked_fill(mask == 0, -1e9)

        # Compute attention probabilities
        attn_probs = F.softmax(scores, dim=-1)
        attn_probs = self.dropout(attn_probs)

        # Save attention weights if requested
        if return_attention:
            self.attention_weights = attn_probs.detach()

        # Apply attention weights to values
        context = torch.matmul(attn_probs, v)

        # Reshape and apply output projection
        context = context.transpose(1, 2).contiguous().view(
            batch_size, -1, self.d_model)
        output = self.out_proj(context)

        if return_attention:
            return output, self.attention_weights
        return output


class FeedForward(nn.Module):
    """Position-wise feed-forward network."""

    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1, activation: str = "relu"):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

        # Support for different activation functions
        if activation == "relu":
            self.activation = F.relu
        elif activation == "gelu":
            self.activation = F.gelu
        else:
            raise ValueError(f"Unsupported activation: {activation}")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input tensor [batch_size, seq_len, d_model]

        Returns:
            Output tensor [batch_size, seq_len, d_model]
        """
        return self.linear2(self.dropout(self.activation(self.linear1(x))))


class EncoderLayer(nn.Module):
    """Transformer encoder layer."""

    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout: float = 0.1, activation: str = "relu"):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
        self.feed_forward = FeedForward(d_model, d_ff, dropout, activation)

        # Layer normalization
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Args:
            x: Input tensor [batch_size, seq_len, d_model]
            mask: Optional mask tensor

        Returns:
            Output tensor [batch_size, seq_len, d_model]
        """
        # Apply pre-norm architecture instead of post-norm (more stable training)
        attn_input = self.norm1(x)
        attn_output = self.self_attn(attn_input, attn_input, attn_input, mask)
        x = x + self.dropout(attn_output)

        ff_input = self.norm2(x)
        ff_output = self.feed_forward(ff_input)
        x = x + self.dropout(ff_output)

        return x


class DecoderLayer(nn.Module):
    """Transformer decoder layer."""

    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout: float = 0.1, activation: str = "relu"):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
        self.cross_attn = MultiHeadAttention(d_model, n_heads, dropout)
        self.feed_forward = FeedForward(d_model, d_ff, dropout, activation)

        # Layer normalization
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self,
                x: torch.Tensor,
                encoder_output: torch.Tensor,
                src_mask: Optional[torch.Tensor] = None,
                tgt_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Args:
            x: Input tensor [batch_size, tgt_len, d_model]
            encoder_output: Encoder output [batch_size, src_len, d_model]
            src_mask: Source mask
            tgt_mask: Target mask (usually causal mask)

        Returns:
            Output tensor [batch_size, tgt_len, d_model]
        """
        # Apply pre-norm architecture for better stability
        attn_input = self.norm1(x)
        self_attn_output = self.self_attn(
            attn_input, attn_input, attn_input, tgt_mask)
        x = x + self.dropout(self_attn_output)

        cross_attn_input = self.norm2(x)
        cross_attn_output = self.cross_attn(
            cross_attn_input, encoder_output, encoder_output, src_mask)
        x = x + self.dropout(cross_attn_output)

        ff_input = self.norm3(x)
        ff_output = self.feed_forward(ff_input)
        x = x + self.dropout(ff_output)

        return x


class TransformerEncoder(nn.Module):
    """Transformer encoder stack."""

    def __init__(self,
                 num_layers: int,
                 d_model: int,
                 n_heads: int,
                 d_ff: int,
                 dropout: float = 0.1,
                 activation: str = "relu"):
        super().__init__()
        self.layers = nn.ModuleList([
            EncoderLayer(d_model, n_heads, d_ff, dropout, activation)
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Args:
            x: Input tensor [batch_size, src_len, d_model]
            mask: Optional mask tensor

        Returns:
            Output tensor [batch_size, src_len, d_model]
        """
        for layer in self.layers:
            x = layer(x, mask)
        return self.norm(x)  # Apply final normalization


class TransformerDecoder(nn.Module):
    """Transformer decoder stack."""

    def __init__(self,
                 num_layers: int,
                 d_model: int,
                 n_heads: int,
                 d_ff: int,
                 dropout: float = 0.1,
                 activation: str = "relu"):
        super().__init__()
        self.layers = nn.ModuleList([
            DecoderLayer(d_model, n_heads, d_ff, dropout, activation)
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)

    def forward(self,
                x: torch.Tensor,
                encoder_output: torch.Tensor,
                src_mask: Optional[torch.Tensor] = None,
                tgt_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Args:
            x: Input tensor [batch_size, tgt_len, d_model]
            encoder_output: Encoder output [batch_size, src_len, d_model]
            src_mask: Source mask
            tgt_mask: Target mask

        Returns:
            Output tensor [batch_size, tgt_len, d_model]
        """
        for layer in self.layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)
        return self.norm(x)  # Apply final normalization


class Transformer(nn.Module):
    """Complete transformer model."""

    def __init__(self,
                 src_vocab_size: int,
                 tgt_vocab_size: int,
                 num_layers: int,
                 d_model: int,
                 n_heads: int,
                 d_ff: int,
                 dropout: float = 0.1,
                 max_len: int = 5000,
                 activation: str = "relu",
                 tie_weights: bool = False,
                 pad_token_id: int = 2):
        super().__init__()
        self.src_vocab_size = src_vocab_size
        self.tgt_vocab_size = tgt_vocab_size
        self.d_model = d_model
        self.pad_token_id = pad_token_id

        # Token embeddings
        self.src_embed = nn.Embedding(
            src_vocab_size, d_model, padding_idx=pad_token_id)
        self.tgt_embed = nn.Embedding(
            tgt_vocab_size, d_model, padding_idx=pad_token_id)

        # Scale embeddings by sqrt(d_model)
        self.embed_scale = math.sqrt(d_model)

        # Positional encoding
        self.positional_encoding = PositionalEncoding(
            d_model, max_len, dropout)

        # Encoder and decoder stacks
        self.encoder = TransformerEncoder(
            num_layers, d_model, n_heads, d_ff, dropout, activation)
        self.decoder = TransformerDecoder(
            num_layers, d_model, n_heads, d_ff, dropout, activation)

        # Output linear layer
        self.output_linear = nn.Linear(d_model, tgt_vocab_size)

        # Tie weights between target embedding and output layer if specified
        if tie_weights and src_vocab_size == tgt_vocab_size:
            self.output_linear.weight = self.tgt_embed.weight

        # Initialize parameters
        self._init_parameters()

    def _init_parameters(self):
        """Initialize model parameters."""
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

    def encode(self, src: torch.Tensor, src_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Encode source sequence.

        Args:
            src: Source token ids [batch_size, src_len]
            src_mask: Source mask [batch_size, 1, src_len]

        Returns:
            Encoder output [batch_size, src_len, d_model]
        """
        src_emb = self.positional_encoding(
            self.src_embed(src) * self.embed_scale)
        return self.encoder(src_emb, src_mask)

    def decode(self,
               tgt: torch.Tensor,
               memory: torch.Tensor,
               tgt_mask: Optional[torch.Tensor] = None,
               memory_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Decode target sequence given encoded memory.

        Args:
            tgt: Target token ids [batch_size, tgt_len]
            memory: Encoder output [batch_size, src_len, d_model]
            tgt_mask: Target mask [batch_size, tgt_len, tgt_len]
            memory_mask: Memory mask [batch_size, tgt_len, src_len]

        Returns:
            Decoder output [batch_size, tgt_len, d_model]
        """
        tgt_emb = self.positional_encoding(
            self.tgt_embed(tgt) * self.embed_scale)
        return self.decoder(tgt_emb, memory, memory_mask, tgt_mask)

    def generate_padding_mask(self, x: torch.Tensor) -> torch.Tensor:
        """
        Generate padding mask for a sequence.

        Args:
            x: Input tensor [batch_size, seq_len]

        Returns:
            Padding mask [batch_size, 1, seq_len]
        """
        # Create a binary mask where padding tokens (pad_token_id) are 0 and others are 1
        mask = (x != self.pad_token_id).unsqueeze(
            1).unsqueeze(2)  # [batch_size, 1, 1, seq_len]
        return mask

    def generate_causal_mask(self, size: int) -> torch.Tensor:
        """
        Generate causal mask for a sequence.

        Args:
            size: Sequence length

        Returns:
            Causal mask [size, size]
        """
        # Create lower triangular matrix (dtype=torch.bool allows direct use with masked_fill)
        mask = torch.triu(torch.ones(size, size),
                          diagonal=1).to(dtype=torch.bool)
        # Convert to binary mask (0/1) with negation
        return ~mask

    def forward(self,
                src: torch.Tensor,
                tgt: torch.Tensor,
                src_mask: Optional[torch.Tensor] = None,
                tgt_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Forward pass through the transformer.

        Args:
            src: Source token ids [batch_size, src_len]
            tgt: Target token ids [batch_size, tgt_len]
            src_mask: Source mask
            tgt_mask: Target mask

        Returns:
            Output logits [batch_size, tgt_len, tgt_vocab_size]
        """
        # Generate masks if not provided
        if src_mask is None:
            src_mask = self.generate_padding_mask(src)

        if tgt_mask is None:
            # Combine padding mask with causal mask
            tgt_padding_mask = self.generate_padding_mask(tgt)
            sq_mask = self.generate_causal_mask(tgt.size(1)).to(tgt.device)
            tgt_mask = tgt_padding_mask & sq_mask

        # Encode source sequence
        encoder_output = self.encode(src, src_mask)

        # Decode target sequence
        decoder_output = self.decode(tgt, encoder_output, tgt_mask, src_mask)

        # Project to vocabulary
        output = self.output_linear(decoder_output)

        return output


# ------------------------------
# Vocabulary and Tokenizer
# ------------------------------

class Vocabulary:
    """Simple vocabulary class."""

    def __init__(self,
                 tokens: Optional[List[str]] = None,
                 special_tokens: Dict[str, int] = None):
        """
        Args:
            tokens: List of tokens to add to vocabulary
            special_tokens: Dictionary of special tokens and their indices
        """
        self.token2id = {}
        self.id2token = {}
        self.next_id = 0

        # Add special tokens
        if special_tokens is None:
            special_tokens = {
                "<s>": 0,      # Start token
                "</s>": 1,     # End token
                "<pad>": 2,    # Padding token
                "<unk>": 3,    # Unknown token
            }

        for token, idx in special_tokens.items():
            self.token2id[token] = idx
            self.id2token[idx] = token
            self.next_id = max(self.next_id, idx + 1)

        # Add other tokens
        if tokens:
            for token in tokens:
                self.add_token(token)

    def add_token(self, token: str) -> int:
        """Add a token to the vocabulary."""
        if token not in self.token2id:
            self.token2id[token] = self.next_id
            self.id2token[self.next_id] = token
            self.next_id += 1
        return self.token2id[token]

    def __len__(self) -> int:
        return len(self.token2id)

    def __getitem__(self, token_or_id: Union[str, int]) -> Union[int, str]:
        """Get token ID from token or token from ID."""
        if isinstance(token_or_id, str):
            return self.token2id.get(token_or_id, self.token2id.get("<unk>", 3))
        elif isinstance(token_or_id, int):
            return self.id2token.get(token_or_id, "<unk>")
        else:
            raise TypeError("Key must be str or int")


class SimpleTokenizer:
    """Simple space-based tokenizer."""

    def __init__(self, vocab: Vocabulary):
        self.vocab = vocab

    def tokenize(self, text: str) -> List[int]:
        """Tokenize text into token IDs."""
        tokens = text.strip().lower().split()
        return [self.vocab[token] for token in tokens]

    def detokenize(self, token_ids: List[int]) -> str:
        """Convert token IDs back to text."""
        tokens = [self.vocab[token_id] for token_id in token_ids]
        # Filter out special tokens for output
        tokens = [t for t in tokens if t not in [
            "<s>", "</s>", "<pad>", "<unk>"]]
        return " ".join(tokens)


# ------------------------------
# Text Generation
# ------------------------------

class TextGenerator:
    """Text generator using transformer model."""

    def __init__(self,
                 model: Transformer,
                 tokenizer: SimpleTokenizer,
                 start_token: str = "<s>",
                 end_token: str = "</s>"):
        self.model = model
        self.tokenizer = tokenizer
        self.start_token_id = self.tokenizer.vocab[start_token]
        self.end_token_id = self.tokenizer.vocab[end_token]

    def generate(self,
                 src_text: str,
                 max_length: int = 30,
                 temperature: float = 1.0,
                 top_k: Optional[int] = None,
                 top_p: Optional[float] = None) -> str:
        """
        Generate text using the transformer model.

        Args:
            src_text: Source text
            max_length: Maximum sequence length to generate
            temperature: Sampling temperature (higher = more random)
            top_k: If set, sample from top k most likely tokens
            top_p: If set, sample from tokens with cumulative probability >= top_p

        Returns:
            Generated text
        """
        device = next(self.model.parameters()).device
        self.model.eval()

        # Tokenize source text
        src_ids = self.tokenizer.tokenize(src_text)
        src_tensor = torch.tensor([src_ids], dtype=torch.long, device=device)

        # Generate source mask
        src_mask = self.model.generate_padding_mask(src_tensor)

        # Encode source sequence
        with torch.no_grad():
            encoder_output = self.model.encode(src_tensor, src_mask)

        # Start with start token
        tgt_ids = [self.start_token_id]

        # Keep generating until we hit max length or end token
        for _ in range(max_length):
            tgt_tensor = torch.tensor(
                [tgt_ids], dtype=torch.long, device=device)
            tgt_mask = self.model.generate_causal_mask(
                tgt_tensor.size(1)).to(device)

            with torch.no_grad():
                # Decode and get logits for next token
                logits = self.model.decode(
                    tgt_tensor, encoder_output, tgt_mask, src_mask)
                next_token_logits = self.model.output_linear(logits[:, -1])

                # Apply temperature
                if temperature != 1.0:
                    next_token_logits = next_token_logits / temperature

                # Apply top-k sampling
                if top_k is not None:
                    indices_to_remove = next_token_logits < torch.topk(
                        next_token_logits, top_k)[0][..., -1, None]
                    next_token_logits[indices_to_remove] = -float('inf')

                # Apply top-p (nucleus) sampling
                if top_p is not None:
                    sorted_logits, sorted_indices = torch.sort(
                        next_token_logits, descending=True)
                    cumulative_probs = torch.cumsum(
                        F.softmax(sorted_logits, dim=-1), dim=-1)

                    # Remove tokens with cumulative probability above the threshold
                    sorted_indices_to_remove = cumulative_probs > top_p
                    # Shift the indices to the right to keep the first token above the threshold
                    sorted_indices_to_remove[...,
                                             1:] = sorted_indices_to_remove[..., :-1].clone()
                    sorted_indices_to_remove[..., 0] = 0

                    # Scatter sorted indices back to original indexing
                    indices_to_remove = sorted_indices_to_remove.scatter(
                        1, sorted_indices, sorted_indices_to_remove)
                    next_token_logits[indices_to_remove] = -float('inf')

                # Sample from the distribution
                probs = F.softmax(next_token_logits, dim=-1)
                next_token_id = torch.multinomial(probs, 1).item()

            # Add the sampled token to our generated sequence
            tgt_ids.append(next_token_id)

            # Check if we've generated an end token
            if next_token_id == self.end_token_id:
                break

        # Convert back to text, removing special tokens
        generated_text = self.tokenizer.detokenize(
            tgt_ids[1:])  # Skip start token

        return generated_text


# ------------------------------
# Main Function
# ------------------------------

def main():
    """Main function for demonstration."""
    # Create vocabulary
    word_list = ["hello", "world", "this", "is", "a", "test", "example",
                 "of", "transformer", "model", "for", "text", "generation", "."]
    vocab = Vocabulary(word_list)

    # Create tokenizer
    tokenizer = SimpleTokenizer(vocab)

    # Transformer parameters
    num_layers = 2
    d_model = 128
    n_heads = 4
    d_ff = 512
    dropout = 0.1
    max_len = 50

    # Create model
    model = Transformer(
        src_vocab_size=len(vocab),
        tgt_vocab_size=len(vocab),
        num_layers=num_layers,
        d_model=d_model,
        n_heads=n_heads,
        d_ff=d_ff,
        dropout=dropout,
        max_len=max_len,
        activation="gelu",  # Use GELU activation
        tie_weights=True    # Tie embedding and output weights
    )

    # Move model to device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    # Create text generator
    generator = TextGenerator(model, tokenizer)

    # Read input text
    print("Enter input text (or press Enter for default):")
    input_text = input().strip()
    if not input_text:
        input_text = "hello world"

    print(f"Input text: '{input_text}'")

    # Generate text
    print("\nGenerating text with various settings:")

    # Default settings
    output_text = generator.generate(input_text)
    print(f"\nDefault generation: '{output_text}'")

    # Higher temperature (more random)
    output_text = generator.generate(input_text, temperature=1.5)
    print(f"Higher temperature (1.5): '{output_text}'")

    # Top-k sampling
    output_text = generator.generate(input_text, top_k=3)
    print(f"Top-k (k=3): '{output_text}'")

    # Top-p sampling
    output_text = generator.generate(input_text, top_p=0.9)
    print(f"Top-p (p=0.9): '{output_text}'")

    print("\nDone!")


if __name__ == "__main__":
    main()
