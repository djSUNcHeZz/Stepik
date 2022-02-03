# процент больших и маленьких символов c и g в строке
string = input()
c = string.upper().count("c".upper())
g = string.upper().count("g".upper())
print((c + g) / len(string) * 100)
