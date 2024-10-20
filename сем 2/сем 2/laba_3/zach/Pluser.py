import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image as Im
from Check import checker

def saving(img, way):
    flag = False
    try:
        img.save(way)
    except Exception:
        mb.showinfo("Ошибка зашифрованного файла", "Указан неверный путь")
        flag = True
    return flag

def add_plus(img):
    width = img.width
    height = img.height
    mina = min(height, width) // 100
    img_list = list(img.getdata())
    i = width // 2 - mina // 2
    for m in range(mina):
        while i < len(img_list):
            img_list[i] = (256, 0, 0)
            i += width
        i = width // 2 - mina // 2 + m + 1
    j = width * (height // 2) - width // 2 - width * (mina // 2)
    for n in range(mina):
        for k in range(width):
            img_list[j + k] = (256, 0, 0)
        j += width
    return img_list

def plus(way, way_out):
    if way == "":
        mb.showinfo("Ошибка исходного файла", "Указан пустой путь")
        return 1
    elif checker(way, "исходного"):
        return 1
    img = Im.open(way)
    img_list = add_plus(img)
    img.putdata(img_list)
    if saving(img, way_out):
        mb.showinfo("Ошибка изменённого файла", "Не удалось сохранить файл")
    img.close()
