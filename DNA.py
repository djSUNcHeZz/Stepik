# подсчет букв идущих подряд в строке
string = input()
count = 1 # беру одну букву
for i in range(len(string) - 1): # последняя буква выпадает из цикла
    if string[i] == string[i + 1]: # сравниваю со следующим
        count += 1 # нашел похожую букву
    else:
        print(string[i] + str(count), end="") # печатаю результат
        count = 1
print(string[-1] + str(count)) # последняя буква
