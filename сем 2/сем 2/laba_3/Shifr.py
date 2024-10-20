from PIL import Image as Im
from Check import *

MAX_LEN = 8

# Функция меняет бит в массиве пикселей
def change_bit(img_list, i, j, x):
    m = str(bin(img_list[i][j])[2:-1]) + x
    return int(m, 2)

# Функция шифрует строку в пиксели изображения
def str_to_bits(text, img_list):
    bt = ''
    text += '\0'
    ind = 0
    for i in range(len(text)):
        x = bin(ord(text[i]))[2:]
        bt = (MAX_LEN - len(x)) * '0' + x
        k = 0
        for j in range(ind, ind + 3):
            a = change_bit(img_list, j, 0, bt[k])
            k += 1
            b = change_bit(img_list, j, 1, bt[k])
            k += 1
            if k == len(bt):
                c = img_list[j][2]
            else:
                c = change_bit(img_list, j, 2, bt[k])
            k += 1
            img_list[j] = (a, b, c)
            if (j + 1) > len(img_list):
                return 1
        ind += 3
    return img_list

# Функция сохраняет новое изображение с проверками пути
def saving(img, way):
    flag = False
    try:
        img.save(way)
    except Exception:
        mb.showinfo("Ошибка зашифрованного файла", "Указан неверный путь")
        flag = True
    return flag
            
# функция взаимодействует с шифруемыми изображениями
def shifr(way, text, way_out):
    if way == "":
        mb.showinfo("Ошибка исходного файла", "Указан пустой путь")
        return 1
    elif checker(way, "исходного"):
        return 1
    img = Im.open(way)
    img_list = list(img.getdata())
    img_list = str_to_bits(text, img_list)
    if img_list == 1:
        mb.showinfo("Ошибка исходного файла", "Строка больше размера изображения")
    img.putdata(img_list)
    if not saving(img, way_out):
        img.show()
    img.close()
        
