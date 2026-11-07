# num = int(input("Введите число: "))


def get_int(text: str) -> int:
    data = input(text)
    num = int(data)
    return num


if __name__ == '__main__':
    number = get_int("Введите целый делитель: ")
    print(f"100 / {number} = {100 / number}")