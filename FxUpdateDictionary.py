def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] += [value]
    elif (key*2) in d.keys():
        d[(key*2)] += [value]
    else:
        d[(key*2)] = [value]
    return

# Вариант 2
'''
def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]
    
приплюсовывает к значению key его же, в случае когда key not in d, в ином случае приплюсовывается 0.
Таким образом, если ключа нет в словаре то выражение вычисляется как:
key += key * 1
Когда ключ уже есть:
key += key * 0
key += 0 # к значению добавляется 0, т.е. оно не изменяется
Это происходит из-за того что результат вычисления выражения key not in d может быть только True или False, которые затем при попытке умножения конвертируются True -> 1, False -> 0.
Далее значение просто добавляется в список.
'''


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)