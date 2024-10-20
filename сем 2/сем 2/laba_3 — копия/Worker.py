import tkinter as tk

from Shifr import *
from Antishifr import *

def fork(doing, stika, way, way_out):
    if doing == "ЗАШИФРОВАТЬ":
        shifr(way.get(), stika.get(), way_out.get())
    elif doing == "РАСШИФРОВАТЬ":
        strk = antishifr(way_out.get())
        stika.delete(0, tk.END)
        stika.insert(0, strk)
    elif doing == "Очистить строку":
        stika.delete(0, tk.END)
    elif doing == "Очистить старт-путь":
        way.delete(0, tk.END)
    elif doing == "Очистить финиш-путь":
        way_out.delete(0, tk.END)
