# вывести сумму всех нечетных чисел в интервале от a до b
#a, b, = int(input().split()), int(input().split())
a, b = (int(i) for i in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    if i % 2 == 1:
        s += i
print(s)