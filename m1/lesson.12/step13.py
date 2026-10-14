def add_nums(num_1, num_2):
    result = num_1 + num_2
    print(result)
    return None


# print(add_nums(1, 2))
# print(add_nums(add_nums(1, 2), add_nums(3, 4)))


res_1 = add_nums(1, 2)
res_2 = add_nums(3, 4)
print(res_1)
print(res_2)

my_result = res_1 + res_2
print(my_result)




