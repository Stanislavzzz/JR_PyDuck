
def get_int(text: str) -> int:
    num = None
    try:
        num = int(input(text))
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

        print(f"Попробуйте еще раз")
    finally:
        return num if isinstance(num, int) else 1


if __name__ == '__main__':
    number = get_int("Введите целый делитель: ")
    print(f"100 / {number} = {100 / number}")