# == != >= <= > <
# from functools import total_ordering


# @total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


person1 = Person("Anna", 27)
person2 = Person("Bob", 27)
person3 = Person("Mary", 31)


print(person1 == person2)
print(person1 != person2)
print(person2 > person3)
print(person2 < person3)
print(person1 > person3)


if person3 > person2:
    print("ОК")