from PIL import Image as Im
import tkinter.messagebox as mb
import tkinter as tk

MAX_LEN = 8

def checker(way, what):
    flag = False
    if way == "":
        mb.showinfo("Ошибка {:}-файла".format(what), "Указан пустой путь")
        flag = True
    else:
        try:
            img = Im.open(way)
            img.close()
        except Exception:
            mb.showinfo("Ошибка {:}-файла".format(what), "По указанному пути нет подходящего изображения")
            flag = True
    return flag

# Функция не даёт вставить ~ в строку 
def is_tilda(key, stika):
    if key.char == '~':
        ind = stika.index(tk.INSERT)
        if ind != 0:
            if stika.get()[ind - 1] == '~':
                # Удаляем ~ из поля ввода
                a = stika.get()
                a = a[:ind - 1] + a[ind:]
                stika.delete(0, tk.END)
                stika.insert(0, a)
                mb.showinfo("Ошибка", "'~' признак окончания строки при шифровании.\
\nСама строка этот символ содержать не должна")
    
