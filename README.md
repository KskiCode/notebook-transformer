# notebook-transformer
Experiments with the basic transformer architecture.

Going back into the fundamentals of transformers with experiments with a basic transformer architecture implemented from scratch. The model is designed for text generation tasks and aims to follow the original transformer architecture described in "Attention Is All You Need".

Training included 3 epochs while running on my local CPU :D (I will try out what my GPU will offer and eventually switch to it as it supports CUDA - we'll see)

## Model Architecture

- **Type**: Decoder-only transformer
- **Parameters**: 93.5M
- **Components**:
  - Multi-head self-attention
  - Position-wise feed-forward networks
  - Layer normalization
  - Positional encodings

## Tokenization

The tokenizer is the gpt2 tokenizer loaded from huggingface (vocab_size=50257).

## Training

To get going, the model is trained on the Brothers Karamasov (downloaded from Project Gutenberg at https://www.gutenberg.org/ebooks/28054). The basic goal is to predict the next token given previous tokens. Training is performed using:

- **Loss Function**: Cross-entropy loss
- **Optimizer**: Adam with learning rate scheduling
- **Regularization**: Dropout for preventing overfitting

## Text Generation

The model supports text generation with the following features:
- Temperature control for adjusting randomness
- Top-k sampling for filtering unlikely tokens
- Configurable maximum sequence length (max_output_tokens)


## Requirements

- PyTorch
- NumPy
- Jupyter Notebook

## Future Work

- Include more text
- Switch to CUDA
- Scale the model to more parameters - see how far it can go locally 

