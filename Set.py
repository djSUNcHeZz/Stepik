# Set - беспорядочные множества с уникальными данными
s = set()

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket) # выдает только уникальные значения в случайном порядке

# поиск значение во множестве
if "orange" in basket:
    print('True')

basket.add('ananas') # добавляет
basket.remove('egg') # выдает ОШИБКУ если элемента нет
basket.discard('egg') # не выдает ошибку при удалении несуществующего элемента
basket.clear() # очищает

for x in basket:
    print(x)
