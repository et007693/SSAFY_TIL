import requests

user_list = []

for i in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    
    if  float(parsed_data['address']['geo']['lat']) < 80 and float(parsed_data['address']['geo']['lng']) > -80:
        user_list.append({'name' : parsed_data['name'], 
                           'lat' : parsed_data['address']['geo']['lat'],
                           'lng' : parsed_data['address']['geo']['lng'],
                           'company' : parsed_data['company']
                        })

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        if censorship(user):
            company = user['company']['name']
            name = user['name']

            if company in censored_user_list:
                censored_user_list[company].append(name)
            else:
                censored_user_list[company] = [name]
                
        else:
            pass

    return censored_user_list

def censorship(user):
    company = user['company']['name']
    name = user['name']
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

print(create_user(user_list))