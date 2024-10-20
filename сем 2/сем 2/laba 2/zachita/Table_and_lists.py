from function import *
import tkinter as tk

def table_lists(table, a, b, h):
    x = list()
    while (h > 0 and a <= b) or (h < 0 and a >= b):
            x.append(a)
            a += h
    y = [f(j) for j in x]
    for i in range(len(x)):
        line = [str(i + 1), '{:^7.2f}'.format(x[i]), '{:^7.2f}'.format(y[i]), '{:^7.2f}'.format(diff(x[i])), '0']
        table.insert('', tk.END, values = line)
    return x, y, a - h
