# Поиск часто встречаемого слова
with open('dataset_3363_3.txt') as file:
    text = list(file.read().replace('\n', " ").lower().split())
    print(text)

max_count = 0
for i in set(text):
    if text.count(i) > max_count:
        word = i
        max_count = text.count(i)
print(word.upper(), max_count)
