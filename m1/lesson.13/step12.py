# numbers = [12, 5, 8, 2, 19, 10, 11, 3]
#
# print(min(numbers))
# print(max(numbers))
#


# all() any()
# my_list = [True, False, True]
# my_list = [True, True, True]
# my_list = ["qwsx", 'qazxs', "", "qasdf"]
# my_list = ["", "", "", ""]
#
# # print(all(my_list))
#
# print(any(my_list))


names = ["Alice", "Bob", "Charlie", "David"]
ages = [12, 34, 53, 23, 121, 123]

# com = zip(names, ages)
# print(list(com))

for name, age in zip(names, ages):
    print(name, age)