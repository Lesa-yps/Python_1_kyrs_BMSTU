from PIL import Image as Im
import tkinter.messagebox as mb
import tkinter as tk

# Функция проверяет путь к файлу
def checker(way, what):
    flag = False
    if way == "":
        mb.showinfo("Ошибка {:} файла".format(what), "Указан пустой путь")
        flag = True
    else:
        try:
            img = Im.open(way)
            img.close()
        except Exception:
            mb.showinfo("Ошибка {:} файла".format(what), "По указанному пути нет подходящего изображения")
            flag = True
    return flag
