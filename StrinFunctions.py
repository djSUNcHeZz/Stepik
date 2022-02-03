string = "ABCD"
for i in string:
    print(i)

# посчитать кол-во B
print(string.count(B))

# индекс B в string
print(string.find(B))

# условие "если B есть в string"
if B in string:
    # заменить B на b
    string.replace("B", "b")

# считает кол-во БОЛЬШИХ B
string.upper().count("b".upper())
