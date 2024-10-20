# (-1)^n * n * x / n!
e, x = map(float, input('Введите точность и х через пробел: ').split())
n = 1
k = (- 1) * x
y = k
while abs(k) > e:
    n += 1
    k *= (- 1) / (n - 1)
    y += k
    print (k)
print ('Cумма бесконечного ряда: {:5.7g}'.format(y))
    
