def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(6))