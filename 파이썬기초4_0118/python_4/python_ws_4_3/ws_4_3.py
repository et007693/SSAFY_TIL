import requests

dummy_data = []

for i in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    
    if  float(parsed_data['address']['geo']['lat']) < 80 and float(parsed_data['address']['geo']['lng']) > -80:
        dummy_data.append({'name' : parsed_data['name'], 
                           'lat' : parsed_data['address']['geo']['lat'],
                           'lng' : parsed_data['address']['geo']['lng'],
                           'company' : parsed_data['company']
                        })

print(dummy_data, sep='\n')