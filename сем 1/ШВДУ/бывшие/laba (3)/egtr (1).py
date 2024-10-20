n, a, b, c = map(int, open('figna1.txt').readline().split())
m = sorted([a, b, c])
k = 0
while n>=m[0]:
    n -= m[0]
    k += 1
if n == 0:
    print (k)
else:
    while n != 0:
        k -= 1
        n += m[0]
        for i in range (1000):
            for j in range (1000):
                if (i*m[1]+j*m[2])==n:
                    print (k+i+j)
                    n = 0
                    break
            if n == 0:
                break

        
