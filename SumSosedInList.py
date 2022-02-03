a = [int(i) for i in input().split()]
if len(a) > 1:
    for n in range(len(a)):
        print(n - 1, n + 1 - len(a))
#        print(a[n - 1] + a[n + 1 - len(a)], end=" ")
else:
    print(*a)