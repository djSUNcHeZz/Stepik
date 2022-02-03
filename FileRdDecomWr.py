#import wget, os
# os.path.join('.', 'dir', 'file.txt')
#www = 'https://stepik.org/api/attempts/187420460/file/dataset_3363_2.txt'
#filename = wget.download(www)
#os.rename(filename, u''+os.getcwd()+'/'+filename)


with open('dataset_3363_2.txt') as d:
    line = list(d.readline().strip())
    print(d)
    print(line)

a = str()
b = str(0)
for i in line:

    if i.isalpha():
        if i != a:

            text = (str(a) * int(b))
            print(text, end='')

            a = i
            b = str()
    else:
        b = b + i
print(text, end='')



# Write byte
#with open('file.txt', 'bw') as inf:
#    inf.write('Some text\n')
#   inf.write(str(25))

# вставляем между символом и цифрой *
# печатаем строку