def sub_nums(num_1, num_2):
    if num_1 > num_2:
        return [num_1 - num_2, num_1 + num_2]
    elif num_1 < num_2:
        return num_2 - num_1, num_1 + num_2
    else:
        result = {
            "sum": num_1 + num_2,
            "sub": num_1 - num_2,
        }
        return result


res_1 = sub_nums(1, 8)
res_2 = sub_nums(20, 3)
res_3 = sub_nums(10, 10)
print(res_1)
print(type(res_1))
print(res_2)
print(type(res_2))
print(res_3)
print(type(res_3))





