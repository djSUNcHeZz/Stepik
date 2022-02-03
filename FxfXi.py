n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])


'''
Для проверки времени исполнения кода:

import time
start_time = time.clock()

# Ваш код...

print ("{:g} s".format(time.clock() - start_time))
'''
