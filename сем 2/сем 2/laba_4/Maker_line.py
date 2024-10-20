# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb

# Константа - размер холста
SIZE_OF_CANVAS = 500

# Создаются координаты прямой
def made_new_x_y(point_x1, point_x2, point_y1, point_y2):
    new_y1 = 0
    new_y2 = SIZE_OF_CANVAS
    new_x1 = point_x1 + (new_y1 - point_y1) * (point_x2 - point_x1) / (point_y2 - point_y1)
    new_x2 = point_x1 + (new_y2 - point_y1) * (point_x2 - point_x1) / (point_y2 - point_y1)
    return new_x1, new_x2, new_y1, new_y2

# Отрисовывается прямая по координатам двух точек
def make_line(cnv, point_x1, point_x2, point_y1, point_y2, color):
    if (point_x2 == point_x1 == point_y1 == point_y2):
            mb.showerror('Ошибка!', "Введена точка.")
            return 1
    if (point_x2 == point_x1 and point_y1 == point_y2):
            new_x1, new_x2, new_y1, new_y2 = 0, SIZE_OF_CANVAS, 0, SIZE_OF_CANVAS
    elif (point_x2 == point_x1):
            new_x1, new_x2, new_y1, new_y2 = made_new_x_y(point_x1, point_x2, point_y1, point_y2)
    elif (point_y2 == point_y1):
            new_y1, new_y2, new_x1, new_x2 = made_new_x_y(point_y1, point_y2, point_x1, point_x2)
    elif abs((point_y2 - point_y1) / (point_x2 - point_x1)) > 1:
            new_x1, new_x2, new_y1, new_y2 = made_new_x_y(point_x1, point_x2, point_y1, point_y2)
    else:
            new_y1, new_y2, new_x1, new_x2 = made_new_x_y(point_y1, point_y2, point_x1, point_x2)
    cnv.create_line(new_x1, new_y1, new_x2, new_y2, fill = color, tag = 'B')
    return 0
