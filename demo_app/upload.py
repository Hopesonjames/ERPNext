import requests
from requests.auth import HTTPBasicAuth

# Your ERPNext/Frappe instance URL
base_url = "http://dcode.com:8002"

# Your API key and secret
api_key = "f291b8c6c43dfb1"
api_secret = "cce88e127d2d794"

# File to upload
file_path = "/home/hopeson/Downloads/unnamed.png"

# API endpoint to upload file
upload_url = f"{base_url}/api/method/upload_file"

# Read the file content
with open(file_path, 'rb') as file:
    # Prepare the request
    files = {
        'file': file,
        'is_private': (None, '1'),  # Set to '0' if the file should be public
    }
    
    # Send the request with SSL verification disabled (for testing purposes)
    try:
        response = requests.post(upload_url, files=files, auth=HTTPBasicAuth(api_key, api_secret), verify=False)
        
        # Check the response
        if response.status_code == 200:
            print("File uploaded successfully")
            print("Response:", response.json())
        else:
            print("Failed to upload file")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)