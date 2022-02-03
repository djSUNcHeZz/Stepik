'''
Напишите программу, на вход которой подаётся прямоугольная матрица
в виде последовательности строк, заканчивающихся строкой,
содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера,
у которой каждый элемент в позиции i, j
равен сумме элементов первой матрицы
на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом
по соответствующему направлению.
'''

a = [] # создаем список - матрицу
b = input()

xN = len(b.split()) # размер матрицы X
yN = 0 # размер матрицы Y

# ввод матрицы
while b != "end":
    a.append([int(i) for i in b.split()]) # добавляем список в список матрицы
    yN += 1 # считаем размер матрицы Y
    b = input() # готовимся к вводу end

# выводим сумму без создания новой матрицы
for y in range(yN):
    for x in range(xN):
        up = a[y - 1][x] # перескок в конец по обратной индексации
        down = a[y + 1 - yN][x] # обратная индексация с перескоком в начало
        left = a[y][x - 1] # перескок в конец по обратной индексации
        right = a[y][x + 1 - xN] # обратная индексация с перескоком в начало
        print(up + down + left + right, end=" ")
    print()
