class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        # return f'{self.name} is {self.age} years old'
        return f'Person("{self.name}", {self.age})'


person1 = Person("John", 18)
person2 = Person("Bob", 27)
person3 = Person("Anna", 31)
# print(person.name)
# print(person.age)
# print(person)
persons = [person1, person2, person3]

print(persons)
print(person1)
print(repr(person1))

print(str(person1))