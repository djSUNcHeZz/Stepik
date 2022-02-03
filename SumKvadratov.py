# вывести сумму квадратов чисел когда их сумма будет равна 0
s_chisel = 0
s_kvadratov = 0
while True:
    a = int(input())
    s_kvadratov += a ** 2
    s_chisel += a
    if s_chisel == 0:
        break
print(s_kvadratov)