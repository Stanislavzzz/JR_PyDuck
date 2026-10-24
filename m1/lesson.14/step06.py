def dec(func):
    def wrapper():
        print("До вызова")
        func()
        print("После вызова")
    return wrapper


# def hello():
#     print('Hello World')


# hello = dec(hello)
# hello()

# hello = dec(hello)()


@dec
def hello():
    print('Hello World')


@dec
def by():
    print('By World')


hello()
by()
hello()