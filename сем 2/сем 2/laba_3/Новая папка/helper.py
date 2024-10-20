# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb
#from PLG import Image as Im

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"235x370+100+200")
window["bg"] = 'aqua'
window.title("Шифратор")
window.resizable(0,0)

# Создаётся строчка "Путь к файлу:"
label1 = tk.Label(text="Путь к файлу:", font = ("Calibry", 11))
label1.grid(row = 0, column = 0, sticky = 'w')

# Создаём окошко ввода и обозначаем его параметры, вставляем в него '0'
way = tk.Entry(justify = tk.RIGHT, font = ("Calibry", 15))
way.grid(row = 0, column = 1, columnspan = 3, stick = 'we', padx = 5)
way.insert(0, 'C:\Users\Олеся\Desktop\panda.png')

# Функция вставит в строку вывода новое значение
##def cleaner(value1):
##    value_main = value1
##    way.delete(0, tk.END)
##    way.insert(0, value1)

# Функция вызывается при нажатии клавиш и (если символ верный) вызывает функцию add_digit
# (если введён ошибочный символ) функция выведет ошибку и приведёт строку вывода в начальное положение
##def chooser(key):
##    del_last(key)
##    key = key.char
##    if key == '':
##        # Если попытались изменить положение курсора, вернёт в конец
##        if way.index('insert') != len(value_main):
##            cleaner(value_main)
##        # Вывод ошибки
##        errors.config(text = '   Неверный ввод.')
##    elif key in ['0', '1', '2', '3', '+', '-', '.', '=', '\r', '\x08']:
##        if key == '\x08': key = '<-'
##        if key == '\r': key = '='
##        add_digit(key)
##    elif key.isdigit():
##        # Вывод ошибки
##        errors.config(text = 'Принимаются числа в 4-сс.')
##    elif key.isalpha():
##        # Вывод ошибки
##        errors.config(text = 'Введите число или знак.')
##    elif key in '*/':
##        # Вывод ошибки
##        errors.config(text = 'Программа + и -.')
##    else:
##        # Вывод ошибки
##        errors.config(text = '   Неверный ввод.')

# Реагирует на нажатие клавиш и вызывает функцию chooser
window.bind('<Key>', chooser)

# Создаём меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаёт вкладку меню "Действия" с выпадающим меню с действиями
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Зашифровать', command = lambda: add_digit('+'))
menu_in.add_command(label = 'Расшифровать', command = lambda: add_digit('-'))
menu_in.add_command(label = 'Очистить строчку', command = lambda: add_digit('C1'))
menu_in.add_command(label = 'Очистить путь', command = lambda: add_digit('C2'))

menu.add_cascade(label = "Действия", menu = menu_in)


# Создаёт вкладку меню "Информация" с выпадающим меню с информацией об авторе и программе
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Программа шифрует строку в изображение и расшифровывает её")

menu.add_cascade(label = "Информация", menu = menu_inf)


# Функция создаёт кнопку
def make_button(digit):
    return tk.Button(text = digit, bd = 7, font = ("Calibry", 13),\
                     command = lambda: add_digit(digit), activebackground = "salmon", bg = "khaki")

# Создаются и отображаются кнопки
make_button('ЗАШИФРОВАТЬ').grid(row = 1, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('РАСШИФРОВАТЬ').grid(row = 1, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('Clean string').grid(row = 1, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('Clean way').grid(row = 1, column = 3, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(2):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строк
window.grid_rowconfigure(1, minsize = 60)

# Включается обработчик событий
window.mainloop()
