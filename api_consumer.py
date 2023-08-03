import requests

def get_api_data(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        print(f"API call failed with status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

def send_post_request(api_url, data):
    try:
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(api_url, json=data, headers=headers)

        if response.status_code == 200:
            return response.json()
        print(f"POST request failed with status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        return None

api_url = "https://api.example.com/post_endpoint"

json_data = {
    "key1": "value1",
    "key2": "value2"
}

if response_data := send_post_request(api_url, json_data):
    print(response_data)
else:
    print("Failed to get a valid response from the API.")


if api_data:
    print(api_data)
else:
    print("Failed to fetch data from the API.")

api_url = "https://simple-user-api-production.up.railway.app/api/user/"
api_data = get_api_data(api_url)
