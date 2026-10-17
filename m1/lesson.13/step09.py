nums = [1, 2, 3, 4, 5, 6, 7]


def x_2(num):
    if num % 2 == 0:
        return True
    return False


nums2 = filter(x_2, nums)
print(list(nums2))


nums2l = filter(lambda x: x % 2 == 0, nums)
print(list(nums2l))

