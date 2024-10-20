# Талышева ИУ7-25Б
# Программа складывает и вычитает вещественные числа в 4-ой системе счисления

# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb
from brain import brain

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"235x370+100+200")
window["bg"] = 'pale green'
window.title("Калькулятор")
window.resizable(0,0)

# Создаём окошко ввода и обозначаем его параметры, вставляем в него '0'
calc = tk.Entry(justify = tk.RIGHT, font = ("Calibry", 15))
calc.grid(row = 0, column = 0, columnspan = 3, stick = 'we', padx = 5)
calc.insert(0, '0')

# Переменная хранит значение в строке вывода
value_main = '0'

# Создаётся строчка "Ответ:"
label3 = tk.Label(text="Ответ:", font = ("Calibry", 11))
label3.grid(row = 1, column = 0, columnspan = 3, sticky = 'w')

# Создаётся строчка для вывода ошибок с начальным значением "   Ошибок нет."
anser = tk.Label(text='', font = ("Calibry", 13))
anser.grid(row = 2, column = 0, columnspan = 3, sticky = 'w')


# Функция вставит в строку вывода новое значение
def cleaner(value1):
    global value_main
    value_main = value1
    calc.delete(0, tk.END)
    calc.insert(0, value1)


# Функция добавляет число в строку вывода или вычисляет выражение
def add_digit(digit):
    # Переменная обозначит нужно ли менять поле ввода
    
    flag = True
    # Обновляется поле ошибок
    errors.config(text = '   Ошибок нет.')
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
                    errors.config(text = 'Вторая точка в числе')
    elif digit in '+-':
        # Если до этого уже был знак, он заменяется на переданный
        if value1[-1] in '+-':
            value1 = value1[:-1] + digit
            # Если последняя точка, программа добавит после неё нуль
        elif value1[-1] == '.':
            value1 += '0' + digit
        elif value1 == '0' and digit == '-':
            value1 = digit
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
        anser.config(text = value1)
        flag = False
    elif digit == '<-':
        # Последний символ в строчке ввода не обрезается, а заменяется нулём
        if len(value1) == 1:
            value1 = '0'
        else:
            value1 = value1[:-1]
    elif digit == 'C1':
        value1 = '0'
    elif digit == 'C2':
        anser.config(text = '')
        flag = False
    # Вызов функции  для вставки в строчку вывода нового значения
    if flag: cleaner(value1)


# Функция удалит последний символ, если в строку вывода что-то добавилось
# и при удалении последнего символа в строке вывода поставит 0
def del_last(key):
    value1 = calc.get()
    if value1 != value_main:
        cleaner(value_main)

# Функция вызывается при нажатии клавиш и (если символ верный) вызывает функцию add_digit
# (если введён ошибочный символ) функция выведет ошибку и приведёт строку вывода в начальное положение
def chooser(key):
    del_last(key)
    key = key.char
    if key == '':
        # Если попытались изменить положение курсора, вернёт в конец
        if calc.index('insert') != len(value_main):
            cleaner(value_main)
        # Вывод ошибки
        errors.config(text = '   Неверный ввод.')
    elif key in ['0', '1', '2', '3', '+', '-', '.', '=', '\r', '\x08']:
        if key == '\x08': key = '<-'
        if key == '\r': key = '='
        add_digit(key)
    elif key.isdigit():
        # Вывод ошибки
        errors.config(text = 'Принимаются числа в 4-сс.')
    elif key.isalpha():
        # Вывод ошибки
        errors.config(text = 'Введите число или знак.')
    elif key in '*/':
        # Вывод ошибки
        errors.config(text = 'Программа + и -.')
    else:
        # Вывод ошибки
        errors.config(text = '   Неверный ввод.')
        

# Реагирует на нажатие клавиш и вызывает функцию chooser
window.bind('<Key>', chooser)

# Создаём меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаёт вкладку меню "Действия" с выпадающим меню с действиями
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Сложить числа', command = lambda: add_digit('+'))
menu_in.add_command(label = 'Вычесть числа', command = lambda: add_digit('-'))
menu_in.add_command(label = 'Очистить поле ввода', command = lambda: add_digit('C1'))
menu_in.add_command(label = 'Очистить поле вывода', command = lambda: add_digit('C2'))
menu_in.add_command(label = 'Удалить 1 символ', command = lambda: add_digit('<-'))
menu_in.add_command(label = 'Вычислить', command = lambda: add_digit('='))

menu.add_cascade(label = "Действия", menu = menu_in)


# Создаёт вкладку меню "Информация" с выпадающим меню с информацией об авторе и программе
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Программа выполняет сложение и вычитание \
вещественных чисел в 4-ой системе счисления."))

menu.add_cascade(label = "Информация", menu = menu_inf)


# Функция создаёт кнопку
def make_button(digit):
    return tk.Button(text = digit, bd = 7, font = ("Calibry", 13),\
                     command = lambda: add_digit(digit), activebackground = "salmon", bg = "khaki")

# Создаются и отображаются кнопки
make_button('C1').grid(row = 3, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('C2').grid(row = 3, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('<-').grid(row = 3, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('1').grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('2').grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('3').grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('0').grid(row = 5, column = 0, stick = 'wens', padx = 5, pady = 5, columnspan = 2)
make_button('.').grid(row = 5, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('+').grid(row = 6, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('-').grid(row = 6, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('=').grid(row = 6, column = 2, stick = 'wens', padx = 5, pady = 5)

# Создаётся строчка "Ошибки:"
label3 = tk.Label(text="Ошибки:", font = ("Calibry", 11))
label3.grid(row = 7, column = 0, columnspan = 3, sticky = 'w')

# Создаётся строчка для вывода ошибок с начальным значением "   Ошибок нет."
errors = tk.Label(text='   Ошибок нет.', font = ("Calibry", 13))
errors.grid(row = 8, column = 0, columnspan = 3, sticky = 'w')

# Задаётсяя минимальный размер колонок
for i in range(9):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строк
for i in range(3, 7):
    window.grid_rowconfigure(i, minsize = 60)

# Включается обработчик событий
window.mainloop()
