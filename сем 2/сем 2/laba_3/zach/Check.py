from PIL import Image as Im
import tkinter.messagebox as mb
import tkinter as tk

def checker(way, what):
    flag = False
    try:
            img = Im.open(way)
            img.close()
    except Exception:
            mb.showinfo("Ошибка {:} файла".format(what), "По указанному пути нет подходящего изображения")
            flag = True
    return flag
