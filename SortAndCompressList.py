# выводить только числа повторящиеся более 1 раза
s = sorted([int(i) for i in input().split()])
for n in set(s):
    if s.count(n) > 1:
        print(n, end=" ")
