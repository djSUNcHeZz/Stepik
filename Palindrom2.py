polindrom = input()
if polindrom.upper() == polindrom.upper()[::-1]:
    print('Yes')
else:
    print('No')
