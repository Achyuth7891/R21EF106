import requests

url = "http://20.244.56.144/test/auth"

# Define the payload (data) to be sent in the POST request
payload = {
    'companyname': 'SABTMED',
    'clientID': '68b43fd0-7d06-4599-a237-1efd5fbc24cf',
    'clientSecret': 'ecPpfMbjmVyGnTbk',
    'ownerName': 'Achyuth',
    'ownerEmail': "geerlaachyuth7891@gmail.com",
    'rollNo': 'R21EF106'
}




# Send the POST request
response = requests.post(url, json=payload)

# Print the response from the server
print(f'Status Code: {response.status_code}')
print(f'Response Body: {response.text}')
