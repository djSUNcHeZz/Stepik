# вывести сумму квадратов чисел когда их сумма будет равна 0
n = int(input())
x = 0
for i in range(1, n + 1):
    for z in range(i):
        x += 1
        if x <= n:
            print(str(i), end=" ")
        else:
            break
