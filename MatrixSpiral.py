'''
Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке
'''
"""
для матрицы 3*3:
                3 ячейки вправо;
2 ячейки ввниз, 2 ячейки влево;
1 ячейка вверх, 1 ячейка вправо
"""
n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]

#print(*list(range(1, n + 1))) # выводим первую строку
#matrix.append([f for f in range(1, n + 1)])
#print(matrix)

N = 0 # число вносимое в ячейки матрицы от 1 до n ** 2

for i in range(0, n): # шаги со сменой направления движения
    # первая строка матрицы
    if i == 0:
        for x in range(i, n ):
            N += 1
            matrix[i][x] = N

    # i%2 = 0 -> yDown xRight
    if i % 2 == 0:
        # заполнение матрицы по Y вниз
        for y in range(i, n - i):
            print(y, n - i)

        # заполнение матрицы по X влево
        for x in range(n - i, i, -1):
            print(n - i, x)

    # i%2 != 0 -> yUp xLeft
    if i % 2 != 0:
        # заполнение матрицы по Y вверх
        for y in range(n - i, i, -1):
            print(y, n - i)

        # заполнение матрицы по X вправо
        for x in range(i, n - i):
            print(n - i, x)

# печать матрицы
for j in range(n):
    for i in range(n):
        print(matrix[j][i], end=" ")
    print()

#### Simple solution http://rosettacode.org/wiki/Spiral_matrix#Python/
def spiral_matrix(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m
for i in spiral_matrix(5): print(*i)


#####
def spiral(n):
    dx, dy = 1, 0  # Starting increments
    x, y = 0, 0  # Starting location
    myarray = [[None] * n for j in range(n)]
    for i in xrange(n ** 2):
        myarray[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray

def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print
            "%2i" % myarray[x][y],
        print

printspiral(spiral(5))

#### Recursive Solution
def spiral(n):
    def spiral_part(x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == (x + 1) and x < (n // 2):
            return spiral_part(x - 1, y - 1, n - 1) + 4 * (n - y)
        if x < (n - y) and y <= x:
            return spiral_part(y - 1, y, n) + (x - y) + 1
        if x >= (n - y) and y <= x:
            return spiral_part(x, y - 1, n) + 1
        if x >= (n - y) and y > x:
            return spiral_part(x + 1, y, n) + 1
        if x < (n - y) and y > x:
            return spiral_part(x, y - 1, n) - 1

    array = [[0] * n for j in xrange(n)]
    for x in xrange(n):
        for y in xrange(n):
            array[x][y] = spiral_part(y, x, n)
    return array


for row in spiral(5):
    print
    " ".join("%2s" % x for x in row)

####
