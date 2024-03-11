number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    increase_user()
    user_info = {'name':name, 'age':age, 'address':address}
    print(f'{name}님 환영합니다!')
    return user_info

many_user = list(map(create_user, name, age, address))

def rental_book(info):
    number = info['age']//10
    name = info['name']
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')
    pass

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')
    pass

user_info = list(map(lambda x: {'name' : x['name'], 'age': x['age']}, many_user))
list(map(rental_book, user_info))