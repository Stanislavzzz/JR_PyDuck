def  add_element_copy(my_list, element):
    new_list = my_list.copy()
    new_list.append(element)
    print(f'В функции my_list - {id(my_list)}')
    print(f'В функции new_list - {id(new_list)}')
    return new_list


numbers = [1, 2, 3, 4, 5]
print(numbers)
print(id(numbers))

numbers = add_element_copy(numbers, 7)
print(numbers)
print(id(numbers))