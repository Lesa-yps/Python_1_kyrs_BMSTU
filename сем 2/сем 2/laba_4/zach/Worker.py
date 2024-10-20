# Импортируем библиотеки
import tkinter as tk
from Mozg import brain

# Функция вызывается в ответ на действия пользователя и выполняет требуемое или вызывает для этого другую функцию
def fork(text, x1, y1, x2, y2, x3, y3, cnv):
    # Из окошек берутся координаты точек
    point_x1 = 0 if x1.get() == '' else int(x1.get())
    point_x2 = 0 if x2.get() == '' else int(x2.get())
    point_x3 = 0 if x3.get() == '' else int(x3.get())
    point_y1 = 0 if y1.get() == '' else int(y1.get())
    point_y2 = 0 if y2.get() == '' else int(y2.get())
    point_y3 = 0 if y3.get() == '' else int(y3.get())
    # Отрисовка 1 точки
    if text == 'Отрисовать\n1 точку':
        i = cnv.create_oval(point_x1 - 1, point_y1 - 1, point_x1 + 1, point_y1 + 1, fill = "red", outline = "red", tag = 'A')
    # Отрисовка 2 точки
    elif text == 'Отрисовать\n2 точку':
        i = cnv.create_oval(point_x2 - 1, point_y2 - 1, point_x2 + 1, point_y2 + 1, fill = "red", outline = "red", tag = 'A')
    # Отрисовка 3 точки
    elif text == 'Отрисовать\n3 точку':
        i = cnv.create_oval(point_x3 - 1, point_y3 - 1, point_x3 + 1, point_y3 + 1, fill = "red", outline = "red", tag = 'A')
    # Отрисовка треугольника
    elif text == 'Построить\nтреугольник':
        cnv.create_line(point_x1, point_y1, point_x2, point_y2, fill = "green")
        cnv.create_line(point_x2, point_y2, point_x3, point_y3, fill = "green")
        cnv.create_line(point_x1, point_y1, point_x3, point_y3, fill = "green", tag = 'B')
    # Вызывается функция brain для построения высоты
    elif text == 'Построить\nвысоту':
        brain(cnv, point_x1, point_x2, point_x3, point_y1, point_y2, point_y3)
    elif text == 'Очистить\nхолст':
        cnv.delete("all")
