# В файле in.txt записаны дробные числа в 8-ричной системе счисления, по одному в строке, разделитель целой и дробной части - точка.
# Требуется:
# 1. Перевести числа из исходного файла в 16-ричную систему счисления и переписать их в файл out1.txt по одному в строке в том же порядке.
# 2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.
# Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается.
# Списки, множества, словари, кортежи для сортировки не использовать.

with open('in.txt', 'w') as f:
    f.write('12.5\n32.7\n234.456\n1.0\n')

with open('in.txt', 'r') as f:
    for i in f:
        print(i, end = '')

def from8_to16(x):
    x = x.rstrip()
    x1 = x.split('.')
    a = 0
    for i in range(len(x)):
        if x[i] != '.':
            a += int(x[i]) * 8**(len(x1[0]) - i - 1)
    a1 = str(a).split('.')
    a1[1], a1[0] = int(a1[1]), int(a1[0])
    a2 = ''
    while a1[0] >= 16:
        m = str(a1[0] % 16)
        k = m
        if m == '10':
            k = 'A'
        elif m == '11':
            k = 'B'
        elif m == '12':
            k = 'C'
        elif m == '13':
            k = 'D'
        elif m == '14':
            k = 'E'
        elif m == '15':
            k = 'F'
        a2 = k + a2
        a1[0] = a1[0] // 16
    m = str(a1[0])
    k = m
    if m == '10':
        k = 'A'
    elif m == '11':
        k = 'B'
    elif m == '12':
        k = 'C'
    elif m == '13':
        k = 'D'
    elif m == '14':
        k = 'E'
    elif m == '15':
        k = 'F'
    a2 = k + a2 + '.'
    a1[1] = float('0.' + str(a1[1]))
    for i in range(5):
        a1[1] *= 16
        m = str(a1[1])[:(str(a1[1]).find('.'))]
        k = m
        if m == '10':
            k = 'A'
        elif m == '11':
            k = 'B'
        elif m == '12':
            k = 'C'
        elif m == '13':
            k = 'D'
        elif m == '14':
            k = 'E'
        elif m == '15':
            k = 'F'
        a2 += k
        a1[1] -= int(m)
        if a1[1] == 0.0:
            break
    return a2
    

f_i = open('in.txt', 'r')
f_o1 = open('out1.txt', 'w')
for i in f_i:
    i = from8_to16(i) + '\n'
    f_o1.write(i)
f_i.close()
f_o1.close()

print()
with open('out1.txt', 'r') as f:
    for i in f:
        print(i, end = '')

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
            if not flag:
                ch_min = i
    if ch_min != None:
        f_o2.write(ch_min)
    f_o1.seek(0)
f_o1.close()
f_o2.close()

print()
with open('out2.txt', 'r') as f:
    for i in f:
        print(i, end = '')


