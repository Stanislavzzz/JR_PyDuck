
def get_int(text: str) -> int:
    is_run = True
    while is_run:

        try:
            num = int(input(text))
            res = 100 / num
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

            print(f"Попробуйте еще раз")
        except ZeroDivisionError as e:
            print(f"Ошибка при делении: {e}")
            res = float("inf")
            break
    return num, res


if __name__ == '__main__':
    number = get_int("Введите целый делитель: ")
    print(f"100 / {number[0]} = {number[1]}")