import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image as Im
from Check import checker
from Pluser import plus

def opener(way, text):
    if way == "":
        mb.showinfo("Ошибка {:} файла".format(text), "Указан пустой путь")
        return 1
    elif checker(way, text):
        return 1
    img = Im.open(way)
    img.show()
    img.close()

def made(doing, way, way_out):
    if doing == "Изменить\nизображение":
        plus(way.get(), way_out.get())
    elif doing == "Вывести\nначальное\nизображение":
        opener(way.get(), "исходного")
    elif doing == "Вывести\nизменённое\nизображение":
        opener(way_out.get(), "изменённого")
        
