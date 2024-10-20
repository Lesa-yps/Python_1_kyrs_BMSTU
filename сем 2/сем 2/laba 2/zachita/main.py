# Талышева Олеся ИУ7-25Б

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk, tkinter.messagebox as mb
from tkinter import ttk
import numpy as np
from Table_and_lists import *

E1 = 0.005
E2 = 1e-5
E3 = 1e-8

def cleaner():
    start.delete(0, tk.END)
    finish.delete(0, tk.END)
    step.delete(0, tk.END)
    hat_table()
    plot_err("Пустой график")

def hat_table():
    heads = ['№ точки', 'xi', 'f(xi)', 'f’(xi)', 'Ошибка']
    table = ttk.Treeview(window, show = 'headings')
    table['columns'] = heads
    for header in heads:
        table.heading(header, text = header, anchor = 'center')
        table.column(header, anchor = 'center')
    table.grid(row = 8, column = 0, columnspan = 5)
    return table

def tables():
    
    table = hat_table()
    try:
        cod = 1
        a = float(start.get())
        cod = 2
        b = float(finish.get())
        if a == b:
            raise ValueError
        cod = 3
        h = float(step.get())
        if h == 0 or h > abs(a - b) or (a < b and h < 0) or (a > b and h > 0):
            raise ValueError
    except Exception:
        line = ['-', '-', '-', '-', str(cod)]
        table.insert('', tk.END, values = line)
        plot_err("Ошибка введённых значений")
    else:
        x, y, new_b = table_lists(table, a, b, h)
        plot_func(x, y, a, new_b)

def plot_err(text):
    figa = Figure(figsize = (4, 4), dpi = 70)
    figa.suptitle(text)

    graf = figa.add_subplot(111)
    graf.grid()

    canvas = FigureCanvasTkAgg(figa, master = window)
    canvas.draw()

    graph_widget = canvas.get_tk_widget()
    graph_widget.grid(row = 0, column = 2, columnspan = 3, rowspan = 7, sticky = 'nsew')

def plot_func(x, y, a, new_b):
    figa = Figure(figsize = (4, 4), dpi = 70)
    figa.suptitle("график функции")
    graf = figa.add_subplot(111)
    graf.plot(x, y, label = "sin(3 * x) + cos(5 * x)")

    x_poi = np.linspace(a, new_b, int(abs(new_b - a) * 1000))
    y_poi = np.array([f(j) for j in x_poi])
    #diff1 = np.array([diff(j) for j in y_poi])
    #diff2 = np.array([diff_2(j) for j in diff1])
    
    
    diff1 = np.diff(y_poi)
    diff2 = np.diff(diff1)
    
    mask = np.abs(y_poi) < E1
    mask1 = np.abs(diff1) < E2
    mask2 = np.abs(diff2) < E3

    graf.scatter(x_poi[:-1][mask1], y_poi[:-1][mask1], color = "yellow", s = 40, marker = 'o', label = "экстремумы")
    graf.scatter(x_poi[:-2][mask2], y_poi[:-2][mask2], color = "red", s = 40, marker = 'v', label = "точки перегиба")
    graf.scatter(x_poi[mask], y_poi[mask], color = "green", s = 40, marker = '*', label = "корни")

    graf.legend()
    graf.grid()

    canvas = FigureCanvasTkAgg(figa, master = window)
    canvas.draw()

    graph_widget = canvas.get_tk_widget()
    graph_widget.grid(row = 0, column = 2, columnspan = 3, rowspan = 7, sticky = 'nsew')
  
def checker(key):
    butt = [start, finish, step]
    if not (key.char).isdigit() and key.char not in "+- .":
        for j in range(len(butt)):
            ind = butt[j].index(tk.INSERT)
            if ind != 0:
                if not (butt[j].get()[ind - 1]).isdigit() and (butt[j].get()[ind - 1]) not in "+- .":
                    a = butt[j].get()
                    a = a[:ind - 1] + a[ind:]
                    butt[j].delete(0, tk.END)
                    butt[j].insert(0, a)
                    mb.showinfo("Ошибка", "Ошибка в поле ввода")
    

window = tk.Tk()
window.geometry(f"1005x505+100+200")
window["bg"] = 'aqua'
window.title("График")
window.resizable(0,0)

what1 = tk.Label(text='Введите начало отрезка:', font = ("Calibry", 13))
what1.grid(row = 0, column = 0, sticky = 'we')

start = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
start.grid(row = 0, column = 1, stick = 'we', padx = 5)

what2 = tk.Label(text='Введите конец отрезка:', font = ("Calibry", 13))
what2.grid(row = 1, column = 0, sticky = 'we')

finish = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
finish.grid(row = 1, column = 1, stick = 'we', padx = 5)

what3 = tk.Label(text='Введите шаг:', font = ("Calibry", 13))
what3.grid(row = 2, column = 0, sticky = 'we')

step = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
step.grid(row = 2, column = 1, stick = 'we', padx = 5)

menu = tk.Menu(window) 
window.config(menu = menu)

menu.add_command(label='Построить', command = lambda: tables())

menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Очистить всё поля', command = lambda: cleaner())
menu_in.add_command(label = 'Очистить ввод начала отрезка', command = lambda: start.delete(0, tk.END))
menu_in.add_command(label = 'Очистить вывод конца отрезка', command = lambda: finish.delete(0, tk.END))
menu_in.add_command(label = 'Очистить ввод шага', command = lambda: step.delete(0, tk.END))

menu.add_cascade(label = "Очистка", menu = menu_in)

menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Программа строит график и \
выводит таблицу с вычисленными значениями шага и функции."))
menu_inf.add_command(label = 'Информация о кодах ошибок', command = lambda: mb.showinfo('Информация о кодах ошибок',\
                                                                                     "0 - программа успешно отработала (ошибок не было)\n\
1 - ошибка во вводе старта\n\
2 - ошибка во вводе финиша\n\
3 - ошибка во вводе шага"))

menu.add_cascade(label = "Информация", menu = menu_inf)

tk.Button(text = "CLEAN", bd = 7, font = ("Calibry", 13), command = lambda: cleaner(), activebackground = "salmon",\
          bg = "khaki").grid(row = 3, column = 0, sticky = 'nswe', padx = 5, pady = 5)

tk.Button(text = "PLOT", bd = 7, font = ("Calibry", 13), command = lambda: tables(), activebackground = "salmon",\
          bg = "khaki").grid(row = 3, column = 1, sticky = 'nswe', padx = 5, pady = 5)

for i in range(4):
    window.grid_columnconfigure(i, minsize = 60)

window.grid_rowconfigure(3, minsize = 60)

window.bind('<Key>', checker)

hat_table()
plot_err("Пустой график")

window.mainloop()
