def dec(func):
    def wrapper():
        print("До вызова")
        func()
        print("После вызова")
    return wrapper


def hello():
    print('Hello World')


hello_new = dec(hello)
hello_new()
