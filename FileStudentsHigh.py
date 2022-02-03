clas_dic = {str(i): [0, 0] for i in range(1,12)}
print(clas_dic)
with open('dataset_3380_5.txt') as file:
    for i in file:
        text = list(i.strip().split())
        #print(text)
        clas_dic[text[0]] += int(text[2]), 0
n = 0
for i in clas_dic.values():
    n += 1
    if sum(i) == 0:
        print(n, "-")
    else:
        print(n, sum(i)/((len(i)-2)/2))