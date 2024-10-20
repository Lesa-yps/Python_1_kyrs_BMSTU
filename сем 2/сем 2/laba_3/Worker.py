import tkinter as tk

from Shifr import *
from Antishifr import *

# Функция, в зависимости от выбранного действия, вызывает нужные функции
# простейшие действия выполняет сама
def fork(doing, stika, stika_out, way, way_out):
    if doing == "ЗАШИФРОВАТЬ":
        shifr(way.get(), stika.get(), way_out.get())
    elif doing == "РАСШИФРОВАТЬ":
        strk = antishifr(way_out.get())
        stika_out.delete(0, tk.END)
        stika_out.insert(0, strk)
    elif doing == "Очистить шифруемую\n строку":
        stika.delete(0, tk.END)
    elif doing == "Очистить расшифрованную\n строку":
        stika_out.delete(0, tk.END)
    elif doing == "Очистить исходный путь":
        way.delete(0, tk.END)
    elif doing == "Очистить выходной путь":
        way_out.delete(0, tk.END)
