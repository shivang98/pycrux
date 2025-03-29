# PyCrux

PyCrux is a Python library that sets up Ollama and local LLMs for users and provides a simple function to summarize text.

## Features

- Checks if Ollama is installed and running.
- Installs Ollama if not found.
- Downloads a default LLM model for summarization.
- Provides a simple function `summarize_text(text)` to generate summaries.

## Installation

```bash
pip install pycrux
```

Or for development:

```bash
pip install -e .
```

## Usage

```python
from pycrux import summarize_text

text = "Ollama is a tool for running large language models locally without an internet connection."
summary = summarize_text(text)
print(summary)
```

## License

This project is licensed under the MIT License.
