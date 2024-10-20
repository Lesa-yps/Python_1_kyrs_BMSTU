# В файле in.txt записаны дробные числа в 8-ричной системе счисления, по одному в строке, разделитель целой и дробной части - точка.
# Требуется:
# 1. Перевести числа из исходного файла в 16-ричную систему счисления и переписать их в файл out1.txt по одному в строке в том же порядке.
# 2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.
# Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается.
# Списки, множества, словари, кортежи для сортировки не использовать.

with open('in.txt', 'w') as f:
    f.write('12.5\n32.7\n234.456\n1.0')

with open('in.txt', 'r') as f:
    for i in f:
        print(i, end = '')

def from8_to16(x):
    x = x.split('.')
    x[1] = x[1].rstrip()
    if len(x[0]) < 3:
        a = '0' * (3 - len(x[0]) % 3) + x[0]
    else:
        a = '0' * (len(x[0]) % 3) + x[0]
    if len(x[1]) < 3:
        b = x[1] + '0' * (3 - len(x[1]) % 3)
    else:
        b = x[1] + '0' * (len(x[1]) % 3)
    print('\n', a, b)
    a2 = 0
    for i in range(len(a)):
        a2 += int(a[i]) * 8**(len(a) - i - 1)
        print('\n', i, a[i])
    print(a2)
##    for i in range(len(a)):
##        a2 += int(a[i]) * 8**(len(a) - i - 1)
##        print('\n', i, a[i])
##    print(a2)

f_i = open('in.txt', 'r')
f_o1 = open('out1.txt', 'w')
for i in f_i:
    i = from8_to16(i)
    f_o1.write(i)
f_i.close()
f_o1.close()

f_o2 = open('out2.txt', 'w')
f_o2.close()

f_o1 = open('out1.txt', 'r')
f_o2 = open('out2.txt', 'r+')
ch_min = 0
while ch_min != None:
    ch_min = None
    for i in f_o1:
        if ch_min == None or len(i) < len(ch_min):
            f_o2.seek(0)
            flag = False
            for j in f_o2:
                if j == i:
                    flag = True
                    break
            if not flag:
                ch_min = i
    if ch_min != None:
        f_o2.write(ch_min)
f_o1.close()
f_o2.close()          
