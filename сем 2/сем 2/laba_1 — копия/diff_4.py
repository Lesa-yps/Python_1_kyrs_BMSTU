# Функция вычитает числа в 4-ой системе счисления
def diff_4(num1, num2):
    # Если необходимо, функция делает числа вещественными и
    # дополняет нулями до одинаковой длины до и после точки
    if '.' not in num1: num1 += '.0'
    if '.' not in num2: num2 += '.0'

    if len(num1[num1.find('.') + 1:]) < len(num2[num2.find('.') + 1:]):
        num1 += '0' * (len(num2[num2.find('.') + 1:]) - len(num1[num1.find('.') + 1:]))
    else:
        num2 += '0' * (len(num1[num1.find('.') + 1:]) - len(num2[num2.find('.') + 1:]))

    if len(num1[:num1.find('.')]) < len(num2[:num2.find('.')]):
        num1 = '0' * (len(num2[:num2.find('.')]) - len(num1[:num1.find('.')])) + num1
    else:
        num2 = '0' * (len(num1[:num1.find('.')]) - len(num2[:num2.find('.')])) + num2
    
    # Если первое число меньше воторого, меняем числа местами и запоминаем минус
    minus = '-' if float(num1) < float(num2) else ''
    if float(num1) < float(num2):
        num1, num2 = num2, num1
    # В переменной differ накапливается разность чисел
    differ = ''
    # Переменная a_old хранит: занималась ли 4 ранее
    a_old = 0

    # Цикл проходится по каждому элементу чисел и вычитает
    # числа последовательно от конца к началу
    for i in range(len(num1)):
        if num1[-1] == '.':
            differ = '.' + differ
        else:
            # Переменная "занимает" разряд, а затем записывается в a_old
            a = 1 if (int(num1[-1]) - a_old) < int(num2[-1]) else 0
            differ = str((int(num1[-1]) - int(num2[-1]) + a * 4 - a_old)) + differ
            a_old = a
        num1 = num1[:-1]
        num2 = num2[:-1]
    
    # Обрезаются лишние 0 с начала и с конца
    while differ[-1] == '0' and differ[-2] != '.':
        differ = differ[:-1]

    while differ[0] == '0' and differ[1] != '.':
        differ = differ[1:]
    # Возвращается результат с минусом, если он был
    return minus + differ
