# функции
def minimum(*a):
    """ добавляет число в список и ищет минимум """
    m = a[0]
    for x in a:
        if x < m:
            m = x
    return m

print(minimum(5, 9, 6, 10))

