import requests

base_url = 'http://dcode.com:8002/api/resource/Students'
auth = ('f291b8c6c43dfb1', '4f8afe8dc2ec454')

regno = "9876"

# Check if the student already exists
response = requests.get(f"{base_url}/{regno}", auth=auth)
if response.status_code == 200:
    print("Student already exists:", response.json())
else:
    # Create
    data = {
        "regno": regno,
        "name1": "run kumar",
        "dob": "2000-01-01",
        "gender": "Male",
        "phone": "7894561235",
        "email_id":"asdrfr@gmail.com"
    }
    response = requests.post(base_url, json=data, auth=auth)
    print("Create:", response.json())

# Read
response = requests.get(f"{base_url}/{regno}", auth=auth)
print("Read:", response.json())

# Update
data = {
    "dob": "2000-01-02"
}
response = requests.put(f"{base_url}/{regno}", json=data, auth=auth)
print("Update:", response.json())

# Delete
response = requests.delete(f"{base_url}/{regno}", auth=auth)
print("Delete:", response.status_code)  # 204 indicates success
