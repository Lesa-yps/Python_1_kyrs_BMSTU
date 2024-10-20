f = open('figna1.txt')
k = 0
flag = 0
while not eof(f):
    a, b, c = map(int, f.readline())
    s = a+b+c
    m = s
    if a%6==b%6==c%6:
        while s>0:
            if s%5==0 or s%5==1:
                flag = 1
        if flag == 0:
            k += 1
print (k)


        
