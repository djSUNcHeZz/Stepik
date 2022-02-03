# Dict - словарь с изменяемыми элементами и неизменяемыми уникальными ключами
dictionary = dict()

dictionary = {1: 'apple', 2: 'orange', 3: 'pear'}

print(dictionary[1])

# поиск значение во множестве
if 1 in dictionary:
    print('True')

dictionary[4] = 'ananas' # добавить
#dictionary[5] # выдает ОШИБКУ если элемента нет
dictionary.get(5) # не выдает ошибку при удалении несуществующего элемента
del dictionary[4] # удалить

# выводит ключи
for x in dictionary:
    print(x)
# или так
for x in dictionary.keys():
    print(x)
# вывод значений
for x in dictionary.values():
    print(x)
# вывод пар
for x in dictionary.items():
    print(x)