# вводятся 3 точки постить треуг и провести высоту из 2

# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb
from Worker import *

# Константа - размер холста
SIZE_OF_CANVAS = 500

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"870x650+100+200")
window["bg"] = 'light pink'
window.title("Решение планиметрических задач")
window.resizable(0,0)

# Создаётся строчка "Координаты 1 точки:"
label1 = tk.Label(text="Координаты 1 точки:", font = ("Calibry", 11))
label1.grid(row = 0, column = 0, columnspan = 4, sticky = 'w')

# Создаётся строчка "x:"
label1_x = tk.Label(text="координата по x:", font = ("Calibry", 11))
label1_x.grid(row = 1, column = 0, sticky = 'w')

# Создаём окошко ввода x и обозначаем его параметры
x1 = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
x1.grid(row = 1, column = 1, stick = 'w', padx = 5)

# Создаётся строчка "y:"
label1_y = tk.Label(text="координата по y:", font = ("Calibry", 11))
label1_y.grid(row = 2, column = 0, sticky = 'w')

# Создаём окошко ввода y и обозначаем его параметры
y1 = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
y1.grid(row = 2, column = 1, stick = 'w', padx = 5)

# Создаётся строчка "Координаты 2 точки:"
label2 = tk.Label(text="Координаты 2 точки:", font = ("Calibry", 11))
label2.grid(row = 3, column = 0, columnspan = 4, sticky = 'w')

# Создаётся строчка "x:"
label2_x = tk.Label(text="координата по x:", font = ("Calibry", 11))
label2_x.grid(row = 4, column = 0, sticky = 'w')

# Создаём окошко ввода x и обозначаем его параметры
x2 = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
x2.grid(row = 4, column = 1, stick = 'w', padx = 5)

# Создаётся строчка "y:"
label2_y = tk.Label(text="координата по y:", font = ("Calibry", 11))
label2_y.grid(row = 5, column = 0, sticky = 'w')

# Создаём окошко ввода y и обозначаем его параметры
y2 = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
y2.grid(row = 5, column = 1, stick = 'w', padx = 5)

# Создаётся строчка "Координаты 3 точки:"
label3 = tk.Label(text="Координаты 3 точки:", font = ("Calibry", 11))
label3.grid(row = 6, column = 0, columnspan = 4, sticky = 'w')

# Создаётся строчка "x:"
label3_x = tk.Label(text="координата по x:", font = ("Calibry", 11))
label3_x.grid(row = 7, column = 0, sticky = 'w')

# Создаём окошко ввода x и обозначаем его параметры
x3 = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
x3.grid(row = 7, column = 1, stick = 'w', padx = 5)

# Создаётся строчка "y:"
label3_y = tk.Label(text="координата по y:", font = ("Calibry", 11))
label3_y.grid(row = 8, column = 0, sticky = 'w')

# Создаём окошко ввода y и обозначаем его параметры
y3 = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
y3.grid(row = 8, column = 1, stick = 'w', padx = 5)

# Создаётся холст
cnv = tk.Canvas(window, width = 500, height = 500, bg = "pink")
cnv.grid(row = 0, column = 2, rowspan = 9, stick = 'wens')

# Создаём меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаёт вкладку меню "Действия" с выпадающим меню с действиями
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Отрисовать 1 точку', command = lambda: fork('Отрисовать\n1 точку', x1, y1, x2, y2, x3, y3, cnv))
menu_in.add_command(label = 'Отрисовать 2 nточку', command = lambda: fork('Отрисовать\n2 точку', x1, y1, x2, y2, x3, y3, cnv))
menu_in.add_command(label = 'Отрисовать 3 точку', command = lambda: fork('Отрисовать\n3 точку', x1, y1, x2, y2, x3, y3, cnv))
menu_in.add_command(label = 'Построить треугольник', command = lambda: fork('Построить\nтреугольник', x1, y1, x2, y2, x3, y3, cnv))
menu_in.add_command(label = 'Построить высоту', command = lambda: fork('Построить\nвысоту', x1, y1, x2, y2, x3, y3, cnv))
menu_in.add_command(label = 'Очистить холст', command = lambda: fork('Очистить\nхолст', x1, y1, x2, y2, x3, y3, cnv))

menu.add_cascade(label = "Действия", menu = menu_in)


# Создаёт вкладку меню "Информация" с выпадающим меню с информацией об авторе и программе
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "По вводенным 3 точкам строится треугольник\
и проводится высота из 2 вершины."))
menu_inf.add_command(label = 'Руководство пользователя', command = lambda: mb.showinfo('Примечания',\
'+ Если координата не введена, но требуется построить прямую или точку, то координата считается равной 0.\n\
+ Размер холста {:}*{:}.".format(SIZE_OF_CANVAS, SIZE_OF_CANVAS'))

menu.add_cascade(label = "Информация", menu = menu_inf)


# Функция создаёт кнопку
def make_button(doing):
    return tk.Button(text = doing, bd = 7, font = ("Calibry", 13),\
                     command = lambda: fork(doing, x1, y1, x2, y2, x3, y3, cnv), activebackground = "salmon", bg = "khaki")

# Создаются и отображаются кнопки
make_button('Отрисовать\n1 точку').grid(row = 9, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('Отрисовать\n2 точку').grid(row = 9, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('Отрисовать\n3 точку').grid(row = 10, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('Построить\nтреугольник').grid(row = 10, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('Построить\nвысоту').grid(row = 9, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить\nхолст').grid(row = 10, column = 1, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(12):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строки с кнопками
for i in range(9, 12):
    window.grid_rowconfigure(i, minsize = 60)

# Функция даёт вставить только +,- и цифры
def checker(key):
    # Создаётся список с названиями окошек ввода
    butt = [x1, x2, x3, y1, y2, y3]
    # Если нажатая кнопка не +,- или цифра
    if not (key.char).isdigit() and key.char not in "+-":
        # Проходимся по всем 5-и окошкам
        for j in range(len(butt)):
            # Считывае позицию курсора в этом окошке
            ind = butt[j].index(tk.INSERT)
            # Если позиция изменилась по сравнению с предыдущей и она не равна 0
            if ind != 0:
                # Если символ не +,- или цифра
                if not (butt[j].get()[ind - 1]).isdigit() and butt[j].get()[ind - 1] not in "+-":
                    # Удаляем невалидный символ из поля ввода
                    a = butt[j].get()
                    a = a[:ind - 1] + a[ind:]
                    butt[j].delete(0, tk.END)
                    butt[j].insert(0, a)
                    mb.showerror('Ошибка!', "Можно вводить только целые числа.")


# Реагирует на нажатие клавиш и вызывает функцию checker
window.bind('<Key>', checker)

# Включается обработчик событий
window.mainloop()
