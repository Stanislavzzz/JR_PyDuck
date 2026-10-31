class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        # print(hash((self.name, self.age)))
        return hash((self.name, self.age))

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        # return f'{self.name} is {self.age} years old'
        return f'Person("{self.name}", {self.age})'


person1 = Person("Anna", 18)
person2 = Person("Bob", 27)
person3 = Person("Anna", 31)

persons = {
    person1: "Дизайнер",
    person2: "Программист",
    person3: "Менеджер",
}

print(persons)
