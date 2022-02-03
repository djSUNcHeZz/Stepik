# среднее чисел которые делятся на 3 в интервале от a до b
a, b = (int(i) for i in input().split()) # ввод через пробел
s = 0 # сумма
n = 0 # кол-во числел
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        n += 1
print(s / n)
