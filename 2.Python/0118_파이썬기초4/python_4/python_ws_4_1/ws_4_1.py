import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(API_URL)
parsed_data = response.json()

print(response)

print(parsed_data)
print(type(parsed_data))

print(parsed_data['name'])
print(parsed_data['username'])
print(parsed_data['company']['name'])
