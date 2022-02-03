# подсчет одинаковых слов в строке
# a aa abC aa ac abc bcd a

# решение через Dict
s = input().lower().split()
d = {}
for i in s:
    d[i] = s.count(i)
for n in d.items():
    print(*n)

# решение через Set
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))

# короткое решение через Set
s = input().lower().split()
print(*['%s %s' %(x, s.count(x)) for x in set(s)], sep='\n')