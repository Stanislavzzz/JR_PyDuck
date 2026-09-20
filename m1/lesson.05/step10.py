# for i in range(10):
#     print(i)


print(list(range(10)))
print(list(range(15)))
print(list(range(7)))

start = 10
stop = 3
print(list(range(start, stop)))

start = 0
stop = 10
print(list(range(stop)))


start = 0
stop = 3
step = 1
print(list(range(stop)))

start = 5
stop = 30
step = 1
print(list(range(start, stop)))

start = 5
stop = 30
step = 2
print(list(range(start, stop + 2, step)))
print(list(range(12, 35, 3)))


start = 35
stop = 3
step = -3
print(list(range(start, stop + 2, step)))