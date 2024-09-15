import requests
import json

class APIDebugger:
    def __init__(self, base_url, api_key, model_name):
        self.base_url = base_url
        self.api_key = api_key
        self.model_name = model_name

    def post(self, endpoint, payload):
        """
        Send a POST request to the specified endpoint with the given payload.

        Args:
            endpoint (str): The API endpoint to hit.
            payload (dict): The JSON payload for the request.

        Returns:
            dict: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        
        # Log the request details for debugging
        self.debug_request(url, payload)

        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.post(url, headers=headers, json=payload)

            # Log the response details for debugging
            self.debug_response(response)

            response.raise_for_status()  # Raise an exception for 4XX/5XX responses
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return {"error": str(e)}

    def debug_request(self, url, payload):
        """
        Log the details of the outgoing request for debugging purposes.
        
        Args:
            url (str): The full URL of the request.
            payload (dict): The payload being sent to the API.
        """
        print("=== API Request ===")
        print(f"URL: {url}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        print("===================")

    def debug_response(self, response):
        """
        Log the details of the API response for debugging purposes.
        
        Args:
            response (requests.Response): The response object.
        """
        print("=== API Response ===")
        print(f"Status Code: {response.status_code}")
        try:
            print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        except json.JSONDecodeError:
            print(f"Response Body: {response.text}")
        print("====================")

    def chat_completion(self, messages):
        """
        Create a chat completion by making a POST request to the API.

        Args:
            messages (list): The list of message dictionaries for the chat history.

        Returns:
            str: The content of the AI's response.
        """
        payload = {
            "model": self.model_name,
            "messages": messages
        }

        response = self.post("v1/chat/completions", payload)
        if "choices" in response and len(response["choices"]) > 0:
            return response["choices"][0]["message"]["content"]
        return "Error: No valid response received."


# Example Usage
if __name__ == "__main__":
    base_url = "http://localhost:1234/v1"
    api_key = "lm-studio"
    model_name = "gpt-4o"

    api_debugger = APIDebugger(base_url, api_key, model_name)

    # Example message payload
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the weather today?"}
    ]

    response = api_debugger.chat_completion(messages)
    print("Final AI Response:", response)