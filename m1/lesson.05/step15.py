is_run = False

for i in range(1, 5):

    for j in range(11, 17):
        print(i, j)
        if j == 14:
            is_run = True
            break

    if is_run:
        break
