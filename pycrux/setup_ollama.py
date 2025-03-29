import shutil
import subprocess
import sys

OLLAMA_INSTALL_URL = "https://ollama.com/download"


def is_ollama_installed():
    """Check if Ollama is installed."""
    return shutil.which("ollama") is not None


def install_ollama():
    """Guide user to install Ollama if not found."""
    print(
        "Ollama is not installed. Please install it manually from:", OLLAMA_INSTALL_URL
    )
    sys.exit(1)


def pull_model(model_name="mistral"):
    """Download a model using Ollama if not already available."""
    if not is_ollama_installed():
        install_ollama()

    print(f"Checking if model '{model_name}' is available...")
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"Model '{model_name}' is ready!")
    except subprocess.CalledProcessError:
        print(f"Failed to download model '{model_name}'. Check Ollama installation.")


def ensure_ollama_setup(model_name="mistral"):
    """Ensure Ollama and the required model are set up."""
    if not is_ollama_installed():
        install_ollama()
    pull_model(model_name)
