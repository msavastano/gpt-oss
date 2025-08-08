import os
import requests

# It is recommended to set your Hugging Face API key as an environment variable.
# You can get your API key from https://huggingface.co/settings/tokens
API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/gpt2"

def query_huggingface_api(payload):
    """
    Queries the Hugging Face Inference API with the given payload.
    """
    if not API_KEY:
        raise ValueError("HUGGINGFACE_API_KEY environment variable not set.")

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    """
    Main function to run the chatbot.
    """
    print("Chatbot initialized. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        payload = {
            "inputs": user_input,
        }

        try:
            api_response = query_huggingface_api(payload)
            # The response format may vary depending on the model.
            # For gpt2, the generated text is in the first element of the list.
            if api_response and isinstance(api_response, list) and 'generated_text' in api_response[0]:
                bot_response = api_response[0]['generated_text']
            else:
                bot_response = f"Error: Unexpected API response format: {api_response}"

            print(f"Chatbot: {bot_response}")

        except requests.exceptions.RequestException as e:
            print(f"Error: Could not connect to the API. {e}")
        except ValueError as e:
            print(e)
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
