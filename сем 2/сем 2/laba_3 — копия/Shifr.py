from PIL import Image as Im
from Check import *

def str_to_bits(text, img_list):
    bt = ''
    text += '~'
    for i in range(len(text)):
        x = bin(ord(text[i]))[2:]
        bt = (MAX_LEN - len(x)) * '0' + x
        add_shifr(img_list, bt, i * MAX_LEN)
    return img_list

def add_shifr(img_list, bt, j):
    for i in range(j, j + len(bt)):
        img_list[i] = (img_list[i][0], img_list[i][1], int(bt[i - j]))

def saving(img, way):
    if way == "":
        mb.showinfo("Ошибка финиш-файла", "Указан пустой путь")
    else:
        try:
            img.save(way)
        except Exception:
            mb.showinfo("Ошибка финиш-файла".format(what), "Указан неверный путь")
            

def shifr(way, text, way_out):
    if checker(way, "старт"):
        return 1
    img = Im.open(way)
    img_list = list(img.getdata())
    img_list = str_to_bits(text, img_list)
    img.putdata(img_list)
    saving(img, way_out)
    img.show()
    img.close()
    
