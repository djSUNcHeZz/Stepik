'''
На вход программе первой строкой передаётся количество D известных нам слов,
после чего на D строках указываются эти слова.
Затем передаётся количество L строк текста для проверки,
после чего L строк текста.
Выведите уникальные "ошибки" в произвольном порядке.
Работу производите без учёта регистра.
'''

D = [input().lower() for x in range(int(input()))]
L = [input().lower().split() for x in range(int(input()))]
s = set()
for i in L:
    for x in i:
        if x not in D:
            s.add(x)
print(*s, sep='\n')

# вариант решения:
# 1) заполняем словарь;
# 2) преобразуем текст в множество слов;
# 3) печатаем разность двух множеств
words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))

#wrd.difference() - выводит разницу в set()
dic = {input().lower() for i in range(int(input()))}
wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}
print(*wrd.difference(dic), sep="\n")
