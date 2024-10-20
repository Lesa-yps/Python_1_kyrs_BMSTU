f_i = open('in1.txt', 'r')
f_o = open('out1.txt', 'w')
f_o.close()
f_o2 = open('out2.txt', 'w')
f_o2.close()
f_o = open('out1.txt', 'r+')

def rom(x):
    x1 = ''
    if x // 1000 > 0:
        x1 += 'M' * (x // 1000)
        x = x % 1000
    if x >= 900:
        x1 += 'CM'
        x -= 900
    if x // 500 > 0:
        x1 += 'D' * (x // 500)
        x = x % 500
    if x >= 400:
        x1 += 'CD'
        x -= 400
    if x // 100 > 0:
        x1 += 'C' * (x // 100)
        x = x % 100
    if x >= 90:
        x1 += 'XC'
        x -= 90
    if x // 50 > 0:
        x1 += 'L' * (x // 50)
        x = x % 50
    if x >= 40:
        x1 += 'XL'
        x -= 40
    if x // 10 > 0:
        x1 += 'X' * (x // 10)
        x = x % 10
    if x == 9:
        x1 += 'IX'
        x -= 9
    if x // 5 > 0:
        x1 += 'V' * (x // 5)
        x = x % 5
    if x == 4:
        x1 += 'IV'
        x -= 4
    x1 += 'I' * x
    return x1

max_len = 0
k = 0
for i in f_i:
    k += 1
    x = int(i.rstrip())
    x = rom(x)
    if len(x) > max_len:
        max_len = len(x)
f_i.seek(0)

for i in f_i:
    x = int(i.rstrip())
    x = rom(x)
    x = ' ' * ((max_len - len(x)) // 2) + x + ' ' * ((max_len - len(x)) - ((max_len - len(x)) // 2)) + '\n'
    f_o.write(x)

f_i.close()
f_i2 = open('in2.txt', 'r')
f_o2 = open('out2.txt', 'r+')

for n in range(1, k+1):
    count = 0
    f_i2.seek(0)
    for i in f_i2:
        if int(i.rstrip()) == n:
            count1 = 0
            f_o.seek(0)
            for j in f_o:
                if count1 == count:
                    f_o2.write(j)
                    break
                count1 += 1
        count += 1

f_i2.close()
f_o2.close()
f_o.close()
        




    
    
