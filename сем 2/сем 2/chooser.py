# импортируем модули
from del_last import del_last
from cleaner import cleaner
from add_digit import add_digit
from err import err

# Функция вызывается при нажатии клавиш и (если символ верный) вызывает функцию add_digit
# (если введён ошибочный символ) функция выведет ошибку и приведёт строку вывода в начальное положение
def chooser(key, errors, calc, value_main):
    del_last(key, calc, value_main)
    key = key.char
    if key == '':
        # Если попытались изменить положение курсора, вернёт в конец
        if calc.index('insert') != len(value_main):
            cleaner(value_main, calc, value_main)
        # Вывод ошибки
        err('   Неверный ввод.')
    elif key in ['0', '1', '2', '3', '+', '-', '.', '=', '\r', '\x08']:
        if key == '\x08': key = '<-'
        if key == '\r': key = '='
        add_digit(key, errors, calc, value_main)
    elif key.isdigit():
        # Вывод ошибки
        err('Принимаются числа в 4-сс.', errors)
    elif key.isalpha():
        # Вывод ошибки
        err('Введите число или знак.', errors)
    elif key in '*/':
        # Вывод ошибки
        err('Программа + и -.', errors)
    else:
        # Вывод ошибки
        err('   Неверный ввод.', errors)
