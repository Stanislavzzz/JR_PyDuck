import random

from step07 import dec_num
from step08 import count_func


@count_func(3)
@dec_num
def func_game(num, count):
    print(f'Число - {num}, Попыток - {count}')
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


    return None

func_game(73, 5)
# res = func_game(115, 13)
