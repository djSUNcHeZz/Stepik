# двумерные списки
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[1]) # выводит первый список
print(a[2][0]) # выводит элемент из списка

# генерация списка 2 способами
n = 3
a = [[0] * n for i in range(n)]
print(a)
a = [[0 for j in range(n)] for i in range(n)]
print(a)
