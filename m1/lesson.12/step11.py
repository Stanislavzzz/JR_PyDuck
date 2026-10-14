def add_nums(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    # result = args[0] + args[1]
    # print(result)


add_nums(1, 2, 3, False, 7.908, num=1, age=2, x=3, name="Bob", is_active=True)





