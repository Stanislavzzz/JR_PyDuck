def update_element(my_dict, key, value):
    my_dict[key] = value
    print(f'В функции {id(my_dict)}')
    return my_dict


info = {"name": "Bob", "age": 23}
print(info)
print(id(info))

info = update_element(info, "age", 25)
print(info)
print(id(info))