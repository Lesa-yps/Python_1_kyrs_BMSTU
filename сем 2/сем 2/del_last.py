# импортируем модуль cleaner
from cleaner import cleaner

# Функция удалит последний символ, если в строку вывода что-то добавилось
# и при удалении последнего символа в строке вывода поставит 0
def del_last(key, calc, value_main):
    value1 = calc.get()
    if value1 != value_main:
        cleaner(value_main, calc, value_main)
        return value_main
