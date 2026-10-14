def add_nums(num, *args, name, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    print(num)
    print(name)
    # result = args[0] + args[1]
    # print(result)


add_nums(100, 1, 5, 7, 2, name="Bob", number=1, age=2, x=3, is_active=True)
# add_nums(1, 2, 3, False, 7.908, num=1, age=2, x=3, name="Bob", is_active=True)





