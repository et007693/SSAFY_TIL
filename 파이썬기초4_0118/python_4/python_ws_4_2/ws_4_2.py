import requests

dummy_data = []

for i in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

print(dummy_data, sep='\n')