# Hugging Face Chatbot

This is a simple chatbot that uses the Hugging Face Inference API to generate responses.

## Prerequisites

- Python 3
- `requests` library

You can install the `requests` library using pip:
```bash
pip install requests
```

## Configuration

1.  **Get a Hugging Face API Key:**
    You need a Hugging Face API key to use this chatbot. You can get one from your Hugging Face account settings: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

2.  **Set the API Key as an Environment Variable:**
    This script reads the API key from an environment variable named `HUGGINGFACE_API_KEY`.

    -   **On macOS and Linux:**
        ```bash
        export HUGGINGFACE_API_KEY='your_api_key_here'
        ```

    -   **On Windows:**
        ```powershell
        $env:HUGGINGFACE_API_KEY='your_api_key_here'
        ```
        Or in Command Prompt:
        ```cmd
        set HUGGINGFACE_API_KEY=your_api_key_here
        ```

    Replace `'your_api_key_here'` with your actual Hugging Face API key.

## Usage

Once you have set the environment variable, you can run the chatbot:

```bash
python chatbot.py
```

The chatbot will initialize, and you can start typing your messages. To exit the chatbot, type `quit`.

## Note on the Model

This chatbot currently uses the `gpt2` model. The original request was for `gpt-oss`, but since I could not confirm the model's availability on the Hugging Face Hub, `gpt2` is used as a replacement. You can change the model by modifying the `API_URL` variable in `chatbot.py`.
