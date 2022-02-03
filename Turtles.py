x, y = 0, 0
for n in range(int(input())):
    m = input().lower().split()
    if m[0] == 'север':
        y += int(m[1])
    elif m[0] == 'юг':
        y -= int(m[1])
    elif m[0] == 'восток':
        x += int(m[1])
    elif m[0] == 'запад':
        x -= int(m[1])
print(x, y)

# решение через dict
d = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
for i in range(int(input())):
    x = input().split()
    d[x[0]] += int(x[1])
print(d['восток'] - d['запад'], d['север'] - d['юг'])
