import random


def count_func(count_game=1):
    print('def count_func')

    def dec_num(func):
        # LOW_NUM = 1
        # UP_NUM = 100
        # LOW_COUNT = 1
        # UP_COUNT = 10

        counter = []

        def wrapper(num1, count1, *args, **kwargs):
            for _ in range(count_game):

                # if num1 < LOW_NUM or num1 > UP_NUM:
                #     num1 = random.randint(LOW_NUM, UP_NUM)
                #
                # if count1 < LOW_COUNT or count1 > UP_COUNT:
                #     count1 = random.randint(LOW_COUNT, UP_COUNT)

                result = func(num1, count1)
                counter.append(result)

            return counter

        return wrapper
    return dec_num


# @count_func(10)
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

# func_game(73, 5)
# res = func_game(75, 7)
