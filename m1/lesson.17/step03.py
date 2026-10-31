class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f'Объект удален - {self.name} is {self.age} years old')



person1 = Person("Anna", 18)
# person2 = Person("Bob", 27)
# person3 = Person("Mary>", 31)

print(person1)

del person1

# print(person1)


