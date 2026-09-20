my_list_1 = [1, 2, 3, 4, 5, 7, 9]
my_list_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
my_list_3 = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "j0"]

# for item1, item2 in zip(my_list_2, my_list_1):
#     print(item1, item2)


for item1, item2, item3 in zip(my_list_2, my_list_1, my_list_3):
    print(item1, item2, item3)

