def make_mul(x):
    def mul(y):
        return x * y
    return mul


mul_by_10 = make_mul(10)
print(mul_by_10)


mul_by_5 = make_mul(5)
print(mul_by_5)

print(mul_by_10(7))
print(mul_by_10(3))
print(mul_by_10(5))


print(mul_by_5(7))
print(mul_by_5(3))
print(mul_by_5(5))
