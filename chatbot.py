import os
import requests

# It is recommended to set your Hugging Face API key as an environment variable.
# You can get your API key from https://huggingface.co/settings/tokens
API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/openai/gpt-oss-120b"

def query_huggingface_api(payload):
    """
    Queries the Hugging Face Inference API with the given payload.
    Handles potential errors like network issues, bad status codes, or non-JSON responses.
    """
    if not API_KEY:
        raise ValueError("HUGGINGFACE_API_KEY environment variable not set.")

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json=payload)

    # Handle non-200 OK responses
    if response.status_code != 200:
        raise requests.exceptions.RequestException(
            f"API request failed with status code {response.status_code}: {response.text}"
        )

    # Handle cases where the response is not valid JSON
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        raise requests.exceptions.RequestException(
            f"Failed to decode JSON response from API. Response text was: '{response.text}'"
        )

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

            # The response format may vary depending on the model and API status.
            # Successful response for gpt2: [{'generated_text': '... '}]
            if api_response and isinstance(api_response, list) and api_response[0].get('generated_text'):
                bot_response = api_response[0]['generated_text']
            # Error response from HF: {'error': '...', 'estimated_time': ...}
            elif isinstance(api_response, dict) and api_response.get("error"):
                bot_response = f"API Error: {api_response['error']}"
                if api_response.get("estimated_time"):
                    bot_response += f" The model may be loading. Please try again in {api_response.get('estimated_time'):.0f} seconds."
            else:
                bot_response = f"Error: Unexpected API response format: {api_response}"

            print(f"Chatbot: {bot_response}")

        except requests.exceptions.RequestException as e:
            print(f"Error: An API error occurred. {e}")
        except ValueError as e: # Catches the missing API key error
            print(e)
            break
        except Exception as e:
            print(f"An unexpected application error occurred: {e}")

if __name__ == "__main__":
    main()
