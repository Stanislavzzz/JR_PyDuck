import random


def dec_num(func):
    print('def dec_num')
    LOW_NUM = 1
    UP_NUM = 100
    LOW_COUNT = 1
    UP_COUNT = 10

    def wrapper(num, count, *args, **kwargs):

        if num < LOW_NUM or num > UP_NUM:
            num = random.randint(LOW_NUM, UP_NUM)

        if count < LOW_COUNT or count > UP_COUNT:
            count = random.randint(LOW_COUNT, UP_COUNT)

        result = func(num, count)

        return result

    return wrapper


# @dec_num
# def func_game(num, count):
#     print(f'Число - {num}, Попыток - {count}')
#     for i in range(count):
#         print(f'Попытка # {i + 1}')
#         answer = int(input('Введите число: '))
#
#         if answer == num:
#             print('Угадал')
#             break
#
#         elif answer > num:
#             print('Твоё число больше')
#         elif answer < num:
#             print('Твоё число меньше')
#     else:
#         print(f'Попытки закончились, загаданное число {num}')
#
#
#     return None
#
# # func_game(73, 5)
# res = func_game(73, 3)
# print(res)
