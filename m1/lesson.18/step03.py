
def get_int(text: str) -> int:
    is_run = True
    while is_run:

        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

            print(f"Попробуйте еще раз")
    return num


if __name__ == '__main__':
    number = get_int("Введите целый делитель: ")
    print(f"100 / {number} = {100 / number}")