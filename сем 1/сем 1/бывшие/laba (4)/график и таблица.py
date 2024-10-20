# Талышева ИУ7-15Б Вариант 18
# Программа по введённым начальному значению, шагу и конечному значению для заданной по варианту функции
# строит таблицу значений этой функции на некотором отрезке и строит её по введенному числу засечек на оси оу график функции

xs, xf, step = map (float, input('Введите через пробел начальное значение, конечное значение и шаг: ').split())
if xs < xf and step > 0 or xs > xf and step < 0:
    t = xs
    print ('-' * 53)
    print ('|', ' ' * 10, 't', ' ' * 10, '|', ' ' * 10, 'z', ' ' * 10, '|')
    print ('-' * 53)
    z_min = 10**10
    z_max = 0
    while xf >= t:
        z = t**7 + 0.456 * t**6 - 0.427 * t**5 + 0.427 * t**4 - 0.482 * t**3 + 0.186 * t**2 - 0.767 * t + 0.205 
        print ('|', ' ' * 3, f'{t:^15.5g}', ' ' * 3, '|', ' ' * 4,  f'{z:^15.5g}', ' ' * 2, '|')
        t += step
        if z > z_max:
            z_max = z
        if z < z_min:
            z_min = z
    print ('-' * 53)
    z_m = z_min

    ser = int(input('Введите число засечек на оси ординат: '))
    sers = ser
    zch = (z_max - z_min) / ser
    while ser > 0:
        if ser == sers:
            print (' ' * 5, f'{z_min:^10.3g}', end = '')
        else:
            print (f'{z_min:^10.5g}', end = '')
        z_min += zch
        ser -= 1
    print ()

    x = 10
    z = 8
    ed = (z_max - z_m) / 85
    print ('{:5.2f}'.format(x), '|', ' ' * int(((z - z_m) * ed - 1)), '*')
    while xf >= t:
        z = t**7 + 0.456 * t**6 - 0.427 * t**5 + 0.427 * t**4 - 0.482 * t**3 + 0.186 * t**2 - 0.767 * t + 0.205
        print ('{:5.2f}'.format(t), '|', ' ' * int(((z - zs) * ed - 1)), '*' , ' ' * int((leng - ((z - zs) * ed - 1) - 3)))
        t += step
else:
    print ('Выполнение невозможно')

