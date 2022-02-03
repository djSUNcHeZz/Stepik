# Более шустрый вариант, где не нужно перебирать всё поле
# Генератор поля для игры Сапер

m, n ,k = (int(i) for i in input().split()) # размеры и количество бомб

# Инициализируем пустое поле
pole = [[0 for i in range(n)] for j in range(m)]

# Вводим координаты бомб (тут косяк)
for bombs in range(k):
    x, y = (int(i) for i in input().split())
    x -= 1
    y -= 1
    pole[x][y] = -1
    for i in [-1, 0, 1]:   # И сразу увеличиваем на единицу значения клеток вокруг бомбы
        for j in [-1, 0, 1]:
            dx = x + i
            dy = y + j
            if dx >= 0 and dx < m and dy >= 0 and dy < n and pole[dx][dy] != -1:
                pole[dx][dy] += 1

# Печатаем поле
for x in range(m):
    for y in range(n):
        cell = pole[x][y]
        if cell == -1:
            print('*', end=' ')
        elif cell == 0:
            print('.', end=' ')
        else:
            print(pole[x][y], end=' ')
    print()