# Импортируем библиотеки
import tkinter as tk
from Mozg import brain
from Maker_line import make_line

# Функция вызывается в ответ на действия пользователя и выполняет требуемое или вызывает для этого другую функцию
def fork(text, x1, y1, x2, y2, cnv):
    # Из окошек берутся координаты точек
    point_x1 = 0 if x1.get() == '' else int(x1.get())
    point_x2 = 0 if x2.get() == '' else int(x2.get())
    point_y1 = 0 if y1.get() == '' else int(y1.get())
    point_y2 = 0 if y2.get() == '' else int(y2.get())
    # Отрисовка основной точки
    if text == 'Отрисовать\nосновную\nточку':
        i = cnv.create_oval(point_x1 - 1, point_y1 - 1, point_x1 + 1, point_y1 + 1, fill = "red", outline = "red", tag = 'A')
    # Отрисовка дополнительной точки
    elif text == 'Отрисовать\nдополнительную\nточку':
        i = cnv.create_oval(point_x2 - 1, point_y2 - 1, point_x2 + 1, point_y2 + 1, fill = "red", outline = "red", tag = 'A')
    # Отрисовка прямой
    elif text == 'Отрисовать\nпрямую':
        make_line(cnv, point_x1, point_x2, point_y1, point_y2, "green")
    # Вызывается функция brain для построения результирующей прямой
    elif text == 'Построить\nрезультирующую\nпрямую':
        brain(cnv, x1, x2, y1, y2)
    # Очищаются окошки ввода координат основной точки
    elif text == 'Очистить\nосновную\nточку':
        x1.delete(0, tk.END)
        y1.delete(0, tk.END)
    # Очищаются окошки ввода координат дополнительной точки
    elif text == 'Очистить\nхолст':
        cnv.delete("all")

# Вставляются новые координаты точки в окошки
def puting(x, y, new_x, new_y):
    x.delete(0, tk.END)
    x.insert(0, str(new_x))
    y.delete(0, tk.END)
    y.insert(0, str(new_y))

# В ответ на нажатие левой кнопкой мышки отрисовывается точка и функцией puting вставляются координаты в окошки
def touch(event, cnv, x1, y1, x2, y2):
    cnv.create_oval(event.x - 1, event.y - 1, event.x + 1, event.y + 1, outline = "red", tag = 'A')
    if (x1.get() != '' and y1.get() != ''):
        puting(x2, y2, event.x, event.y)
    else:
        puting(x1, y1, event.x, event.y)
