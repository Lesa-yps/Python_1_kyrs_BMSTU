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
        m = len(i.split(' '))
    for i in range(m):
        for k in range(n):
            f_i.seek(0)
            c = 0
            for j in f_i:
                if c == (n - k - 1):
                    l = j.rstrip().split(' ')
                    if k == (n - 1):
                        l[i] = l[i] + '\n'
                    else:
                        l[i] = l[i] + ' '
                    f_o.write(l[i])
                c += 1
    f_i.close()

print() 
with open('out.txt', 'r') as f:
    for i in f:
        print(i, end = '')
