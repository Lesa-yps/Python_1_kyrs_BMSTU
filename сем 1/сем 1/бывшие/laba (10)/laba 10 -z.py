# Талышева Иу7-15Б
# Метод трапеций

import math as m

def First_Fun(x):
    y = - m.cos(x)
    return y

def fun(x):
    y = m.sin(x)
    return y

st, fin = map(float, input('Введите начало и конец отрезка интегрирования через пробел: ').split())
if fin < st:
    fin, st = st, fin

leng = fin - st

N1, N2 = map(int, input('Введите количества участков разбиения через пробел: ').split())

def box(N):
    leng_P = leng / N
    st_P = st
    S = 0
    for i in range(N):
        fin_P = st_P + leng_P
        sr_line = (fun(st_P) + fun(fin_P)) / 2
        S += abs(sr_line * leng_P)
        st_P += leng_P
    return S

def Int(S):
    dif = abs(S - (First_Fun(fin) - First_Fun(st)))
    return dif

S_box_N1 = box(N1)
print('С разбиением N1 = {} интеграл = {:5.2f}, точность = {:5.2f}.'.format(N1, S_box_N1, Int(S_box_N1)))

S_box_N2 = box(N2)
print('С разбиением N2 = {} интеграл = {:5.2f}, точность = {:5.2f}.'.format(N2, S_box_N2, Int(S_box_N2)))

if Int(S_box_N1) < Int(S_box_N2):
    print('с разбиением {} точность больше'.format(N1))
elif Int(S_box_N1) == Int(S_box_N2):
    print('точности равны')
else:
    print('с разбиением {} точность больше'.format(N2))

E = float(input('Введите точность: '))

n = 1
while abs(box(n * 2) - box(n)) >= E:
    n *= 2
print('Искомая точность для метода трапеций достигается при следующем количестве итераций: ', n)
