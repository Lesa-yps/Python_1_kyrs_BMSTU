# Импортируем модули diff_4 и sum_4
from diff_4 import diff_4
from sum_4 import sum_4

# Функция отрабатывает, когда получает на вход = и вычисляет результат выражения
def brain(value):
    # Если + или - в выражении нет, функция вернёт само выражение
    if '+' not in value and '-' not in value:
        return value
    else:
        # num1 хранит первое число, которое складывается/вычитается
        num1 = None
        # Пока длина выражения больше нуля цикл будет работать
        while len(value) > 0:
            # num2 хранит второе число, которое складывается/вычитается
            num2 = ''
            # Цикл "собирает" числа для вычисления
            while value[0] not in '+-':
                num2 += value[0]
                value = value[1:]
                if len(value) == 0:
                    break
            # Записывается значение в num1, запоминается знак
            if num1 == None:
                num1 = num2
                sign = value[0]
                value = value[1:]
                if num1 == '':
                    num1 = '0'
            # Если "собраны" оба числа
            else:
                # Проверка на перый минус
                minus = ''
                if float(num1) < 0 and sign == '-':
                    minus = '-'
                    num1 = num1[1:]
                    sign = '+'
                elif float(num1) < 0 and sign == '+':
                    num1 = num1[1:]
                    num1, num2 = num2, num1
                    sign = '-'
                # Числа складываются/вычитаются
                if sign == '+':
                    num1 = sum_4(num1, num2)
                else:
                    num1 = diff_4(num1, num2)
                num1 = minus + num1
                # Если выражение закончилось, возвращаем результат (num1)
                if len(value) == 0:
                    return num1
                # Иначе запоминаем знак и обрезаем выражение до следующего числа
                else:
                    sign = value[0]
                    value = value[1:]
