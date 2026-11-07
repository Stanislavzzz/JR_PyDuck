
def get_int(text: str) -> int:
    data = input(text)

    try:
        num = int(data)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        num = 1
        print(f"Наше новое значение : {num=}")
    return num


if __name__ == '__main__':
    number = get_int("Введите целый делитель: ")
    print(f"100 / {number} = {100 / number}")