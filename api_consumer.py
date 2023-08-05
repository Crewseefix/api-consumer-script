import requests
import json

# function that sends a get request to the api
def send_get_request(api_url):
    try:
        response = requests.get(api_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

# function that sends a post request to the api
def send_post_request(api_url, data):
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(api_url, json=data, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        return None

# function that sends a patch request to the api
def send_patch_request(api_url, data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(api_url, data=json.dumps(data), headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to make PATCH request. Status code: {response.status_code}")
        return None
    
# function that sends a delete request to the api
def send_delete_request(api_url, data=None):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(api_url, json=data, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to make DELETE request. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Data to send in requests
    get_url = "https://simple-user-api-production.up.railway.app/api/user/"
    create_url = "https://simple-user-api-production.up.railway.app/api/user/"
    patch_url = "https://simple-user-api-production.up.railway.app/api/user/1/"
    delete_url = "https://simple-user-api-production.up.railway.app/api/user/1/"
    create_multiple_url = "https://simple-user-api-production.up.railway.app/api/user/updates/"
    patch_multiple_url = "https://simple-user-api-production.up.railway.app/api/user/updates/"
    delete_multiple_url = "https://simple-user-api-production.up.railway.app/api/user/updates/"
    createDeleteUpdate_multiple_url = "https://simple-user-api-production.up.railway.app/api/user/createdeleteandupdate/"
    data_to_create = {
        "first_name": "Harry",
        "last_name": "Potter",
        "username": "@harry_potter",
        "email": "harry.potter@hogwarts.edu"
    }
    data_to_create_multiple ={
        "data": [
            {
               "first_name": "Harry",
                "last_name": "Potter",
                "username": "@harry_potter",
                "email": "harry.potter@hogwarts.edu" 
            },
            {
                "first_name": "Hermione",
                "last_name": "Granger",
                "username": "@hermione_granger",
                "email": "hermione.granger@hogwarts.edu"
            }
        ]
    }
    data_to_patch = {
        "first_name": "Harry",
        "last_name": "Potter",
    }
    data_to_patch_multiple = {
        "data": [
            {
               "first_name": "Harry",
                "last_name": "Potter"
            },
            {
                "first_name": "Hermione",
                "last_name": "Granger"
            }
        ]
    }
    data_to_delete_multiple = {
        "data": ["1", "2"]
    }
    data_to_createDeleteUpdate_multiple = {
        "data":
            [
                {
                    "id": "1"
                },
                {
                    "id": "1",
                    "first_name": "Harry"
                },
                {
                    "first_name": "Harry",
                    "last_name": "Potter",
                    "username": "@harry_potter",
                    "email": "harry.potter@hogwarts.edu"
                }
            ]
    }
    
    # Sending requests and printing responses
    # get users
    if response_data := send_get_request(get_url):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to fetch data from the API.")
    # creeate a user
    if response_data := send_post_request(create_url, data=data_to_create):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")
    # patch a user
    if response_data := send_patch_request(patch_url, data=data_to_patch):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")  
    # delete a user
    if response_data := send_delete_request(delete_url):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")
    # create multiple users
    if response_data := send_post_request(create_multiple_url, data=data_to_create_multiple):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")
    # patch multiple users
    if response_data := send_patch_request(patch_multiple_url, data=data_to_patch_multiple):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")  
    # delete multiple users
    if response_data := send_delete_request(delete_multiple_url, data=data_to_delete_multiple):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")
    # create, delete and update multiple users
    if response_data := send_post_request(createDeleteUpdate_multiple_url, data=data_to_createDeleteUpdate_multiple):
        print(response_data)
        print("\n\n")
    else:
        print("Failed to get a valid response from the API.")