class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        self.user_data['name'] = input('이름을 입력하세요 : ')
        try:
            self.user_data['age'] = int(input('나이를 입력하세요 : '))
        except:
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        if 'name' and 'age' not in self.user_data.keys():
            print('사용자 정보가 입력되지 않았습니다.')
        else:
            name = self.user_data['name']
            age = self.user_data['age']
            print(f'사용자 정보 : \n이름 : {name}\n나이 : {age}')

user = UserInfo()
user.get_user_info()
user.display_user_info()
