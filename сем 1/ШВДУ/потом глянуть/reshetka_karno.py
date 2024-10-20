# решетка кардано
#  программа, которая будет шифровать или расшифровывать сообщение по алгоритму кардано

import random
# считывание файла
import os
def innamefile():
    name1 = ''
    while name1 == '':
        name1 = str(input('Введите название файла: '))
        if name1 == '':
            print('Введите корректное название файла: ')
    try:
        f1 = open(name1  + 'key.txt', mode = 'r')
        f2 = open(name1  + 'matrix.txt', mode = 'r')
    except IOError:
        f1 = open(name1 + 'key.txt', mode = 'w')
        f2 = open(name1 + 'matrix.txt', mode = 'w')
    f1.close()
    f2.close()


def CreateMatrix():
    # создаем матрицу - шаг 1
    M = [[None for j in range 8] for i in range(8)]
    for i in range(4):
        for j in range(4):
            M[i][j] = i*4 + j + 1 # заполнится квадрат слева сверху
            M[j][7 - i] = i*4 + j  + 1# заполнится квадрат справа сверху
            M[7-j][i] = i*4 + j + 1 # заполнится квадрат слева снизу
            M[7 - i][7-j] = i*4 + j + 1 # заполнится квадрат справа снизу

    # вырезаем числа, создаем решетку
    # принцип: идем по числам от 1 до 16 и рандомно выбираем в каком квадрате число удалить(прировнять к None)
    for v in range(1,17):
        p = random.randint(0,4) # номер квадрата
        i, j = (v-1)//4, (v-1)%4
        if p == 0:
            M[i][j] = None
        elif p == 1:
            M[j][7 - i] = None
        elif p == 2:
            M[7 - j][i] = None
        elif p == 3:
            M[7 - i][7 - j] = None

    # делаем матрицу бинарной
    for i in range(8):
        for j in range(8):
            if M[i][j] is None:
                M[i][j] == '1'
            else:
                M[i][j] == '0'

    return M

#создадим массив, элементы которого - десятичная запись "значения" строки - последняя фотка

















