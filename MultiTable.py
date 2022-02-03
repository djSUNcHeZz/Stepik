# таблица умножения
a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d + 1):
    print("\t", i, end="")
print()
for a in range(a, b + 1):
    print(a, end="")
    for x in range(c, d + 1):
        print("\t", a * x, end="")
    print()
