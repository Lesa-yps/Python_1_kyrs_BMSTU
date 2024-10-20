# Функция складывает числа в 4-ой системе счисления
def sum_4(num1, num2):
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

    # В переменной summa накапливается суммма чисел
    summa = ''

    # Переменная а отвечает за переполнение разряда   
    a = 0

    # Цикл проходится по каждому элементу чисел и складывает
    # числа последовательно от конца к началу
    for i in range(len(num1)):
        if num1[-1] == '.':
            summa = '.' + summa
        else:
            summa = str((int(num1[-1]) + int(num2[-1]) + a) % 4) + summa
            a = (int(num1[-1]) + int(num2[-1]) + a) // 4
        num1 = num1[:-1]
        num2 = num2[:-1]

    # Добавляем переполнение разряда, если оно было
    if a == 1:
        summa = '1' + summa
    
    return summa
