import tkinter as tk

def brain(cnv, point_x1, point_x2, point_x3, point_y1, point_y2, point_y3):
    if (point_x1 == point_x3):
        y = point_y2
        x = point_x1
    elif (point_y1 == point_y3):
        y = point_y1
        x = point_x2
    else:
        y = ((point_x2 - point_x1) / 2) * ((point_y3 - point_y1) / (point_x3 - point_x1)) + point_y2 / 2 + point_y1 / 2
        x = point_x2 - (y - point_y2) * ((point_x3 - point_x1) / (point_y3 - point_y1))
    cnv.create_line(point_x2, point_y2, int(x), int(y), fill = "blue", tag = 'B')
