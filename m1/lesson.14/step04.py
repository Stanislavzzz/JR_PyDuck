def guess_num(num, count):
    def func_game():
        for i in range(count):
            print(f'Попытка # {i + 1}')
            answer = int(input('Введите число: '))

            if answer == num:
                print('Угадал')
                break

            elif answer > num:
                print('Твоё число больше')
            elif answer < num:
                print('Твоё число меньше')
        else:
            print(f'Попытки закончились, загаданное число {num}')

    return func_game


game = guess_num(32, 5)
game1 = guess_num(37, 7)
print(game)

game()
game1()