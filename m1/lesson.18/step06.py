res = None
is_run = True

while is_run:

    try:
        num = int(input("Введите число: "))
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        print(f"Попробуйте еще раз")
    else:
        try:
            res = 100 / num
        except ZeroDivisionError as e:
            res = float('inf')
        break

print(f"{res=}")