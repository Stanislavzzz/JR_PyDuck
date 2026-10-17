nums = [1, 2, 3, 4, 5, 6, 7]

# lambda x: x ** 2

def x_3(num):
    return num ** 3

sq_nums = map(lambda x: x ** 2, nums)
print(list(sq_nums))

str_nums = map(lambda x: str(x), nums)
print(list(str_nums))

nums3 = map(x_3, nums)
print(list(nums3))

s_nums = map(str, nums)
print(list(s_nums))