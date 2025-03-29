import ollama


def summarize_text(text, model_name, word_count=50):
    """Summarize the given text using Ollama's local LLM."""

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that summarizes text concisely.",
        },
        {
            "role": "user",
            "content": f"Summarize the following text in less than {word_count} words:\n\n{text}",
        },
    ]

    try:
        response = ollama.chat(model=model_name, messages=messages)
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Error while summarizing: {e}"
