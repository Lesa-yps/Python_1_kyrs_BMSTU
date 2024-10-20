# Талышева ИУ7-15Б
# Программа в данном списке строк находит самую длинную, являющуюся
# чередованием цифр и латинских букв

a = [str(i) for i in input('Введите элементы массива через пробел: ').split()]
fin = ''
for i in range(len(a)):
    flag = True
    num = 0
    alf = 0
    if str.isdigit(a[i][0]):
        num = 1
    if 65 <= ord(a[i][0]) <= 90 or 97 <= ord(a[i][0]) <= 122:
        alf = 1
    for j in range(1, len(a[i])):
        if num == 1 and (65 <= ord(a[i][j]) <= 90 or 97 <= ord(a[i][j]) <= 122):
            num = 0
            alf = 1
        elif alf == 1 and str.isdigit(a[i][j]):
            alf = 0
            num = 1
        else:
            flag = False
            break
    if flag and (len(a[i]) > len(fin)):
        fin = a[i]
if fin == '':
    print('Такой строки нет')
else:
    print('Самая длинная, являющаяся чередованием цифр и латинских букв, строка: ', fin)
