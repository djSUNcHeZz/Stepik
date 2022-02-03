'''
считывает файл с подобной структурой и для каждого абитуриента
выводит его среднюю оценку по этим трём предметам на отдельной строке,
соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите
средние баллы по математике, физике и русскому языку по всем абитуриентам.
'''

summa_mat = 0
summa_phiz = 0
summa_rus = 0
n = 0
with open('dataset_3363_4.txt') as file:
    for i in file:
        text = list(i.strip().split(';'))
        srednee_student = round(((float(text[1]) + float(text[2]) + float(text[3])) / 3), 9)
        print(srednee_student)
        n += 1
        summa_mat += float(text[1])
        summa_phiz += float(text[2])
        summa_rus += float(text[3])
    sredee_mat = round(summa_mat / n, 9)
    srednee_phiz = round(summa_phiz / n, 9)
    srednee_rus = round(summa_rus / n, 9)
    print(sredee_mat, srednee_phiz, srednee_rus)

