import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as m
import tkinter as tk, tkinter.messagebox as mb
from tkinter import ttk
import numpy as np
# импорт модуля
from change import *

# константы
E1 = 0.005

# Вычисляет значение введённой функции
def f(x):
    fx = func.get()
    new_fx = changer(fx)
    return eval(new_fx)

# Очистка всех полей ввода, графика и таблицы
def cleaner():
    # Очистка всех полей ввода
    func.delete(0, tk.END)
    start.delete(0, tk.END)
    finish.delete(0, tk.END)
    step.delete(0, tk.END)
    itera.delete(0, tk.END)
    border.delete(0, tk.END)
    # Очистка графика
    plot_err("Пустой график")

# Функция вызывает функцию построения графика
def tables():
    # вызывается функция построения графика и проверка входных данных
    try:
        cod = 1
        if func.get() == '':
            raise "Error with function"
        cod = 5
        a = float(start.get())
        cod = 6
        b = float(finish.get())
        if a == b:
            raise "Error with sides"
        cod = 7
        h = float(step.get())
        if (a > b and h > 0) or (a < b and h < 0) or h == 0 or h > abs(b - a):
            raise "Error with step"
        cod = 8
        N_max = int(itera.get())
        if N_max < 0:
            raise "Error with max iter"
        cod = 9
        eps = float(border.get())
        if eps <= 0:
            raise "Error with eps"
        cod = 0
        a_n = a
        was = False
        try:
            while (h > 0 and a_n <= b) or (h < 0 and a_n >= b):
                f(a_n)
                a_n += h
        except Exception:
            cod = 1
            for i in range(-10000, 10000, 100):
                try:
                    f(i)
                except Exception:
                    pass
                else:
                    was = True
                    cod = 11
        else:
            was = True
        if cod == 11 and was:
            raise "Error with step"
        if cod == 1 and was:
            raise "Error with function"
        plot_func()
    # при ошибочных входных данных в таблицу выводится код ошибки 1
    except Exception as e:
        print(e)
        plot_err("Ошибка введённых значений")
        
    errors.config(text = cod)
            

# Создаёт списки координат
def make_lists(a, b):
    h = float(step.get())
    u = 0.01
    i = a
    x = []
    while (h > 0 and i <= b) or (h < 0 and i >= b):
            i += u
            x.append(i)
    y = [f(j) for j in x]
    while (h > 0 and a <= b) or (h < 0 and a >= b):
            a += h
    return x, y, a - h

# Функция строит пустой график
def plot_err(text):

    # Cоздание графика функции
    figa = Figure(figsize = (4, 4), dpi = 70)
    figa.suptitle(text)

    graf = figa.add_subplot(111)
    graf.grid()

    canvas = FigureCanvasTkAgg(figa, master = window)
    canvas.draw()

    graph_widget = canvas.get_tk_widget()
    graph_widget.grid(row = 0, column = 2, columnspan = 6, rowspan = 9, sticky = 'nsew')

# Функция строит график
def plot_func():

    a = float(start.get())
    b = float(finish.get())

    # Вызов функции для создания списков координат
    x, y, new_b = make_lists(a, b)

    # Cоздание графика функции
    figa = Figure(figsize = (4, 4), dpi = 70)
    figa.suptitle("График функции")
    graf = figa.add_subplot(111)
    graf.plot(x, y, label = "график функции")

    # Нахождение корней
    x_poi = np.linspace(a, new_b, int(abs(new_b - a) * 1000))
    y_poi = np.array([f(j) for j in x_poi])
    
    mask = np.abs(y_poi) < E1

    # Отрисовка корней
    graf.scatter(x_poi[mask], y_poi[mask], color = "green", s = 40, marker = '*', label = "корни")

    # Отрисовка легенды и графика
    graf.legend()
    graf.grid()

    canvas = FigureCanvasTkAgg(figa, master = window)
    canvas.draw()

    graph_widget = canvas.get_tk_widget()
    graph_widget.grid(row = 0, column = 2, columnspan = 6, rowspan = 9, sticky = 'nsew')
        
# Функция не даёт вставить букву в последние 5 окошек    
def checker(key):
    # Создаётся список с названиями окошек ввода
    butt = [start, finish, step, itera, border]
    # Если нажатая кнопка - буква
    if not (key.char).isdigit() and key.char not in "+- .":
        # Проходимся по всем 5-и окошкам
        for j in range(5):
            # Считывае позицию курсора в этом окошке
            ind = butt[j].index(tk.INSERT)
            # Если позиция изменилась по сравнению с предыдущей и она не равна 0
            if ind != 0:
                if (butt[j].get()[ind - 1]).isalpha():
                    # Удаляем букву из поля ввода
                    a = butt[j].get()
                    a = a[:ind - 1] + a[ind:]
                    butt[j].delete(0, tk.END)
                    butt[j].insert(0, a)
    

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"900x280+100+200")
window["bg"] = 'light grey'
window.title("График")
window.resizable(0,0)

# Создаются текстовые подсказки и поля ввода для входных данных
# Для формулы - функции
what1 = tk.Label(text='Введите функцию:', font = ("Calibry", 13))
what1.grid(row = 0, column = 0, sticky = 'we')

func = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
func.grid(row = 0, column = 1, stick = 'we', padx = 5)

# Для начала отрезка
what2 = tk.Label(text='Введите начало отрезка:', font = ("Calibry", 13))
what2.grid(row = 1, column = 0, sticky = 'we')

start = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
start.grid(row = 1, column = 1, stick = 'we', padx = 5)

# Для конца отрезка
what3 = tk.Label(text='Введите конец отрезка:', font = ("Calibry", 13))
what3.grid(row = 2, column = 0, sticky = 'we')

finish = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
finish.grid(row = 2, column = 1, stick = 'we', padx = 5)

# Для шага итерации
what4 = tk.Label(text='Введите шаг:', font = ("Calibry", 13))
what4.grid(row = 3, column = 0, sticky = 'we')

step = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
step.grid(row = 3, column = 1, stick = 'we', padx = 5)

# Для максимального количества итераций
what4 = tk.Label(text='Введите макc кол-во итераций:', font = ("Calibry", 13))
what4.grid(row = 4, column = 0, sticky = 'we')

itera = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
itera.grid(row = 4, column = 1, stick = 'we', padx = 5)

# Для точности
what5 = tk.Label(text='Введите точность:', font = ("Calibry", 13))
what5.grid(row = 5, column = 0, sticky = 'we')

border = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
border.grid(row = 5, column = 1, stick = 'we', padx = 5)


# Создаётся меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаётcя вкладка меню "Построить", строящая график и таблицу
menu.add_command(label='Построить', command = lambda: tables())

# Создаётся вкладка меню "Очистка" с выпадающим меню с вариантами очистки
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Очистить всё поля', command = lambda: cleaner())
menu_in.add_command(label = 'Очистить ввод функции', command = lambda: func.delete(0, tk.END))
menu_in.add_command(label = 'Очистить ввод начала отрезка', command = lambda: start.delete(0, tk.END))
menu_in.add_command(label = 'Очистить вывод конца отрезка', command = lambda: finish.delete(0, tk.END))
menu_in.add_command(label = 'Очистить ввод шага', command = lambda: step.delete(0, tk.END))
menu_in.add_command(label = 'Очистить ввод max кол-ва итераций', command = lambda: itera.delete(0, tk.END))
menu_in.add_command(label = 'Очистить ввод точности', command = lambda: border.delete(0, tk.END))

menu.add_cascade(label = "Очистка", menu = menu_in)

# Создаётся вкладка меню "Информация" с выпадающим меню с информацией об авторе, программе и кодах ошибок
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Марина"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Программа строит график и \
выводит таблицу уточнения корня функции."))
menu_inf.add_command(label = 'Информация о кодах ошибок', command = lambda: mb.showinfo('Информация о кодах ошибок',\
                                                                                     "0 - программа успешно отработала (ошибок не было)\n\
1 - ошибка во вводе функции\n\
2 - максимальное количество итераций достигнуто при точности, меньшей заданной\n\
3 - деление на нуль при уточнении корня\n\
4 - ошибка при уточнении корня\n\
5 - ошибка во вводе начала отрезка\n\
6 - ошибка во вводе конца отрезка\n\
7 - ошибка во вводе шага\n\
8 - ошибка во вводе максимального количества итераций\n\
9 - ошибка во вводе точности\n\
10 - корней на отрезке не найдено\n\
11 - ошибка во вводе отрезка"))

menu.add_cascade(label = "Информация", menu = menu_inf)

# Создаётся и отображается кнопка очистки всех полей
tk.Button(text = "CLEAN ALL", bd = 7, font = ("Calibry", 13), command = lambda: cleaner(), activebackground = "salmon",\
          bg = "khaki").grid(row = 6, column = 0, sticky = 'nswe', padx = 5, pady = 5)

# Создаётся и отображается кнопка построения графика и таблицы
tk.Button(text = "PLOT", bd = 7, font = ("Calibry", 13), command = lambda: tables(), activebackground = "salmon",\
          bg = "khaki").grid(row = 6, column = 1, sticky = 'nswe', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(9):
    window.grid_columnconfigure(i, minsize = 70)

# Задаётсяя минимальный размер строки с кнопками
window.grid_rowconfigure(6, minsize = 60)

# Реагирует на нажатие клавиш и вызывает функцию checker
window.bind('<Key>', checker)

# Создаётся строчка "Ошибки:"
label3 = tk.Label(text="Код ошибки:", font = ("Calibry", 11))
label3.grid(row = 7, column = 0, columnspan = 3, sticky = 'w')

# Создаётся строчка для вывода ошибок с начальным значением "   Ошибок нет."
errors = tk.Label(text='0', font = ("Calibry", 13))
errors.grid(row = 8, column = 0, columnspan = 3, sticky = 'w')

# Начальное построение графика
plot_err("Пустой график")

# Включается обработчик событий
window.mainloop()
