# найти минимум в списке
a = [int(i) for i in input().split()]
minimum = a[0]
for n in a:
    if n < minimum:
        minimum = n
print(minimum)
