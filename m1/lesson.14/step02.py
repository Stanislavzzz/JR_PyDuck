def outer(name):
    def inner():
        print(f"Привет, {name}!")
    return inner


hello_ivan = outer('Ivan')
print(hello_ivan)
print(type(hello_ivan))
print(id(hello_ivan))

hello_bob = outer('Bob')
print(hello_bob)
print(type(hello_bob))
print(id(hello_bob))


hello_bob()
hello_ivan()
