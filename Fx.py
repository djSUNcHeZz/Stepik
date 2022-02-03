# функция модифицирует ГЛОБАЛЬНЫЙ список
def modify_list(l):
    r = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            r.append(l[i] // 2)
    l[:] = r
    return l

lst = [1, 3, 3, 7]
modify_list(lst)
print(lst)
