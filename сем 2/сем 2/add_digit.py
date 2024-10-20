# Импортируем модули cleaner и brain
from cleaner import cleaner
from brain import brain
from err import err

# Функция добавляет число в строку вывода или вычисляет выражение
def add_digit(digit, errors, calc, value_main):
    # Обновляется поле ошибок
    err('   Ошибок нет.', errors)
    # Cчитывается значение в строке ввода
    value1 = calc.get()
    # Переданное значение добавляется в строку вывода с проверками
    if digit in '0123':
        if value1[-1] in '123.+-':
            value1 += digit
        elif value1[-1] == '0':
            if len(value1) == 1:
                value1 = digit
            elif value1[-2] in '+-':
                # Лишний нуль в начале заменяется
                value1 = value1[:-1] + digit
            else:
                value1 += digit
    elif digit == '.':
            # Добавляется ноль, если число начало вводится с точки
            if value1[-1] in '+-':
                value1 += '0.'
            else:
                # Проверка на существование точки в числе (не вводится ли вторая точка)
                value2 = value1
                flag = True
                while len(value2) > 0 and value2[-1] not in "+-":
                    if value2[-1] == '.':
                        flag = False
                        break
                    else:
                        value2 = value2[:-1]
                if flag:
                    value1 += digit
                else:
                    # Вывод ошибки
                    err('Вторая точка в числе', errors)
    elif digit in '+-':
        # Если до этого уже был знак, он заменяется на переданный
        if value1[-1] in '+-':
            value1 = value1[:-1] + digit
            # Если последняя точка, программа добавит после неё нуль
        elif value1[-1] == '.':
            value1 += '0' + digit
        elif value1[-1] in '1230':
            value1 += digit
    elif digit == '=':
        # Перед последним знаком поставит 0
        if value1[0] in '+-':
            value1 = '0' + value1
        # Если последний был знак, то он удаляется
        if value1[-1] == '+' or value1[-1] == '-':
            value1 = value1[:-1]
        value1 = brain(value1)
    elif digit == '<-':
        # Последний символ в строчке ввода не обрезается, а заменяется нулём
        if len(value1) == 1:
            value1 = '0'
        else:
            value1 = value1[:-1]
    elif digit == 'C':
        value1 = '0'
    # Вызов функции  для вставки в строчку вывода нового значения
    cleaner(value1, calc, value_main)
