import requests
import json

def call_lambda_api():
    # Replace with the actual API Gateway endpoint
    api_url = "https://7beoa231p1.execute-api.us-east-1.amazonaws.com/testLogs"
    
    # Example payload
    payload = {
        "candidate_id": "12345",
        "log_content": """[2024-01-07 10:15:30] ERROR: Database connection failed
[2024-01-07 10:15:35] INFO: Retry attempt 1
[2024-01-07 10:15:40] ERROR: Authentication failed"""
    }

    try:
        # Send POST request to the API Gateway endpoint
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Print the response
        print("API Response:")
        print(json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException as e:
        print(f"Error calling the API: {e}")

if __name__ == "__main__":
    call_lambda_api()
