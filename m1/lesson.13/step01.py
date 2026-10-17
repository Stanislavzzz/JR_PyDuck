def  add_element(my_list, element):
    my_list.append(element)
    print(f'В функции {id(my_list)}')
    return my_list


numbers = [1, 2, 3, 4, 5]
print(numbers)
print(id(numbers))

numbers = add_element(numbers, 7)
print(numbers)
print(id(numbers))