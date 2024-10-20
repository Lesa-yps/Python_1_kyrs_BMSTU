from math import sqrt
x1, y1 = map(int, input("Введите координаты точки a: ").split())
x2, y2 = map(int, input("Введите координаты точки b: ").split())
x3, y3 = map(int, input("Введите координаты точки c: ").split())
a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
b = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a,b,c)
p=(a+b+c)/2
bis = 2*sqrt(p*(p-a)*(p-b)*(p-c))/a
print("Расстояние биссектрисы: {:.5g}".format(bis))
