import time


def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


def fibonachi_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        memo[n] = fibonachi_memo(n - 1, memo) + fibonachi_memo(n - 2, memo)
        return memo[n]


# start_1 = time.time()
# print(fibonachi(40))
# end_1 = time.time() - start_1
# print(f"Время выполнения {end_1:7f} секунд")

start_2 = time.time()
print(fibonachi_memo(500))
end_2 = time.time() - start_2
print(f"Время выполнения {end_2:7f} секунд")
