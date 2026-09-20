my_list = [1, 2, 3, 4, True, 'qaz']


# for item in enumerate(my_list):
#     print(item)

# for index, item in enumerate(my_list):
#     print(index, item)


for index, item in enumerate(my_list, start=10):
    print(index, item)