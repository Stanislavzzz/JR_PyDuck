class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        return f"Ув. {self.name} is {self.age * 10} years old"


person1 = Person("Anna", 27)
person2 = Person("Bob", 27)
person3 = Person("Mary", 31)


print(person1())

#
# __iter__
# __next__
# __enter__
# __exit__