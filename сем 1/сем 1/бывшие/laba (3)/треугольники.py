# Талышева ИУ7-15Б
# Программа по введенным целочисленным координатам трех точек на плоскости вычисляет длины сторон
# образованного треугольника и длину медианы, проведенной из наименьшего угла.
# Определяет: является ли треугольник остроугольным.
# По введённым координатам точки определяет: находится ли точка внутри треугольника.
# Если да, то находит расстояние от точки до наиболее удаленной
# стороны треугольника или ее продолжения.

eps = 0.0001

# Ввод координат точек
x1, y1 = map(int, input('Введите координаты первой точки через пробел: ').split())
x2, y2 = map(int, input('Введите координаты второй точки через пробел: ').split())
x3, y3 = map(int, input('Введите координаты третьей точки через пробел: ').split())

#сохраняем введённые значения в другие переменные 
x10, x20, x30, y10, y20, y30 = x1, x2, x3, y1, y2, y3

# Считаем уравнение прямой для второй и третьей точек
if x2 != x3:
    a = (y2 - y3) / (x2 - x3)
    b = y2 - a * x2
    f = a*x1 + b
    flag = 0
else:
    f = x2
    flag = 1

# Проверяем являются ли введенные координаты совпадающими
# В этом случае введена точка
if x1 == x2 == x3 and y1 == y2 == y3:
    print ('Это точка')
# Проверяем лежат ли точки на 1 прямой
elif (flag == 0 and f == y1) or (flag == 1 and f == x1):
    print ('Это прямая')
else:
    # Вычисляем длины сторон треугольника и сортируем по возрастанию
    length12 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    length23 = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    length31 = ((x3 - x1)**2 + (y3 - y1)**2)**0.5
    #сохраняем вычисленные значения в другие переменные
    a = length12
    b = length23
    c = length31
    if length12 > length23:
        length12, length23 = length23, length12
    if length23 > length31:
        length23, length31 = length31, length23
    if length12 > length23:
        length12, length23 = length23, length12
    # Вычисляем длину медианы
    median = ((2 * length31**2 + 2 * length23**2 - length12**2) / 4)**0.5

    # Вывод длин сторон и медианы
    print ('Длины сторон: {:5.6}, {:5.6}, {:5.6}'.format(length12, length23, length31))
    print ('Длина медианы, проведенной из наименьшего угла: {:5.6}'.format(median))

    # Проверяем треугольник на остроугольность и выводим результат
    if eps < (length12**2 + length23**2 - length31**2):         # По теореме Пифагора
        print ('Треугольник является остроугольным')
    else:
        print ('Треугольник не является остроугольным')

    # Вводим координаты точки
    x0, y0 = map(int, input('Введите координаты точки через пробел: ').split())

    # Cортируем по возрастанию x введённые координаты
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    if x2 > x3:
        x2, x3 = x3, x2
        y2, y3 = y3, y2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    # Находим уравнения прямых, задающих стороны треугольника
    if x1 != x2:
        a12 = (y1 - y2)/(x1 - x2)
        b12 = y1 - a12*x1
        f12 = a12*x0 + b12
    else:
        f12 = x1
    if x2 != x3:
        a23 = (y3 - y2)/(x3 - x2)
        b23 = y2 - a23*x2
        f23 = a23*x0 + b23
    else:
        f23 = x2
    if x1 != x3:
        a31 = (y1 - y3)/(x1 - x3)
        b31 = y3 - a31*x3
        f31 = a31*x0 + b31
    else:
        f31 = x3

    if x1 <= x0 <= x3:
        # Если проверяемая точка лежит между крайними х треугольника
        # Разбиваем треугольник по средней вершине и проверяем точку на нахождение между у
        # Если проверяемая точка лежит между х и у треугольника, то она лежит внутри треугольника, иначе не лежит
        if  x1 <= x0 <= x2 and (f31 <= y0 <= f12 or f12 <= y0 <= f31):
            print ('Точка лежит внутри треугольника')
            sign = 1
        elif  x2 < x0 <= x3 and (f31 <= y0 <= f23 or f23 <= y0 <= f31):
            print ('Точка лежит внутри треугольника')
            sign = 1
        else:
            print('Точка не лежит внутри треугольника')
            sign = 0
    # Если проверяемая точка не лежит между крайними х треугольника, то она не лежит внутри треугольнника
    else:
        print('Точка не лежит внутри треугольника')
        sign = 0

    # Считаем расстояния от точки до вершин треугольника
    if sign == 1:
        length10 = ((x10 - x0)**2 + (y10 - y0)**2)**0.5
        length20 = ((x20 - x0)**2 + (y20 - y0)**2)**0.5
        length30 = ((x30 - x0)**2 + (y30 - y0)**2)**0.5

        # Считаем полупериметр треугольника с вершинами в точках 0, 1, 2 и вычисляем
        # кратчайшее расстояние от точки до стороны треугольника или ее продолжения
        half_meter = (length10 + length20 + a)/2
        height1 = 2 * (half_meter * (half_meter - length10) * (half_meter - length20) * (half_meter - a))**0.5 / a
        height = height1
        # Считаем полупериметр треугольника с вершинами в точках 0, 1, 3 и вычисляем
        # кратчайшее расстояние от точки до стороны треугольника или ее продолжения
        half_meter = (length10 + length30 + c)/2
        height2 = 2 * (half_meter * (half_meter - c) * (half_meter - length30) * (half_meter - length10))**0.5 / c
        if height2 > height: height = height2
        # Считаем полупериметр треугольника с вершинами в точках 0, 2, 3 и вычисляем
        # кратчайшее расстояние от точки до стороны треугольника или ее продолжения
        half_meter = (length20 + length30 + b)/2
        height3 = 2 * (half_meter * (half_meter - length20) * (half_meter - length30) * (half_meter - b))**0.5 / b
        if height3 > height: height = height3
        # Находим максимальное расстояние и выводим его
        print ('Расстояние от точки до наиболее удаленной стороны треугольника или ее продолжения: {:5.6}'.format(height))
