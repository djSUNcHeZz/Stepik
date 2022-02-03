# вывод индеска числа в списке
lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    for n in range(len(lst)):
        if lst[n] == x:
            print(n, end=" ")
