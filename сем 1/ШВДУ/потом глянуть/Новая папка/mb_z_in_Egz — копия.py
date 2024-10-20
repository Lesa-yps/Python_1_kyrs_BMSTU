#запись поворота квадратной матрицы в другой файл

with open('in.txt', 'w') as f:
    f.write('1 2 3 4\n\
5 6 7 8\n\
9 10 11 12\n\
13 14 15 16\n')

with open('in.txt', 'r') as f:
    for i in f:
        print(i, end = '')

with open('out.txt', 'w') as f_o:
    pass
    
with open('out.txt', 'r+') as f_o:
    f_i = open('in.txt', 'r')
    n = 0
    for i in f_i:
        n += 1
    for j in range(n):
        f_i.seek(0)
        c = 0
        x = ''
        #len_old = 0
        for i in f_i:
            #f_o.seek(0)#(-1) * len_old, 1)
            l = i.rstrip().split(' ')
            #print(i, l[j])
            if c == 0:
                l[j] = l[j] + '\n'
            else:
                l[j] = l[j] + ' '
            x = l[j] + x
            c += 1
            #f_o.write(l[j])
            #len_old = len(l[j])
        f_o.write(x)
    f_i.close()

print() 
with open('out.txt', 'r') as f:
    for i in f:
        print(i, end = '')
