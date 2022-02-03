import os
os.path.join('source/1', 'dir', 'file.txt')

# Readline from file
with open('file.txt') as inf:
    for line in inf:
        line = line.strip()
        s1 = inf.readline().strip()


# Write byte
with open('file.txt', 'bw') as inf:
    inf.write('Some text\n')
    inf.write(str(25))
