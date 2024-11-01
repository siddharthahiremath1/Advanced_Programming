import requests

# The API endpoint
url = "https://lvsite.madum.cc"

headers={
        'User-Agent': 'python-requests/2.31.0',
    }
# A GET request to the API
response = requests.get(url, verify=False,headers=headers)


# Print the response
print(response)