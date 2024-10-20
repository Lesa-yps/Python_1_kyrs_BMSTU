from PIL import Image as Im
from Check import *
import tkinter.messagebox as mb

MAX_LEN = 8

# функция расшифровывает строку
def get_shifr(img_list):
    strk = ''
    simbol = ''
    i = 0
    flag = True
    try:
        while flag:
            for j in range(MAX_LEN):
                simbol += str(img_list[i + (j // 3)][j % 3] & 1)
            strk += chr(int(simbol, 2))
            simbol = ''
            if strk[-1] == '\0':
                flag = False
            i += 3
    except Exception:
        strk = ""
    return strk[:-1], flag

# функция взаимодействует с изображением и возвращает расшифрованную строку
def antishifr(way):
    if checker(way, "зашифрованного"):
        return ""
    img = Im.open(way)
    img_list = list(img.getdata())
    img.close()
    strk, flag = get_shifr(img_list)
    if flag:
        mb.showinfo("Ошибка зашифрованного файла", "Строка не была записана")
        return ""
    return strk
    
