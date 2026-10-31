class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        return f"Ув. {self.name} is {self.age * 10} years old"

    @staticmethod
    def info():
        print("Информация")

    @classmethod
    def new_person(cls):
        print("Создаю нового пользователя")
        return cls("Mila", 7)

    @classmethod
    def my_person(cls, name, age):
        print("Создаю нового пользователя")
        return cls(name, age)

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        # return f'{self.name} is {self.age} years old'
        return f'Person("{self.name}", {self.age})'


def my_info():
    print("Моя информация")

person1 = Person("Anna", 27)
person2 = Person("Bob", 27)
person3 = Person("Mary", 31)


person1.info()
my_info()
Person.info()

print()

new_user = person1.new_person()
print(new_user)

new_user1 = person1.my_person("Alice", 19)
print(new_user1)

print(Person.my_person("Anna", 29))