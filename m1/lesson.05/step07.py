number = 10


while True:
    print(number)
    number -= 1
    if number == 0:
        is_running = False

    if number < 5:
        break

    print('YES')

print('ОК')