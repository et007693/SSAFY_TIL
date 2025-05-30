class Person:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_method()

    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')

    @classmethod
    def class_method(cls):
        cls.number_of_people += 1

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
