# импортируем библиотеки
import math
import tkinter as tk
import pygame
from random import randint

# константы
length = 40
step = 10
clock_size = 40
monk_y = 120
monk_x = 360
clock_xy = 100
bord_1 = 90
bord_2 = 410
ticki = 25
center_kitten = 50

# функция задаёт новые координаты котика для приближения его к кругу
def new_coord(x, y, x_c, y_c):
    
    new_x = x
    new_y = y
    
    if (abs(x - x_c) < step):
        new_x = x_c
    elif (x_c > x):
        new_x += step
    elif (x_c < x):
        new_x -= step

    if (abs(y - y_c) < step):
        new_y = y_c
    elif (y_c > y):
        new_y += step
    elif (y_c < y):
        new_y -= step

    return new_x - center_kitten, new_y - center_kitten

# функция вычисляет рандомные координаты, не заезжающие на существующие картинки
def right():
    x1 = randint(bord_1, bord_2)
    y1 = randint(bord_1, bord_2)
    while (x1 >= monk_x and y1 <= monk_y) or (x1 <= clock_xy and y1 <= clock_xy):
        x1 = randint(bord_1, bord_2)
        y1 = randint(bord_1, bord_2)
    return x1, y1

# функция отрисовывает треугольник
def treg(okno, x1, y1):
    pygame.draw.line(okno, 'red', (x1, y1 - 5), (x1 - 5, y1 + 5), width = 5)
    pygame.draw.line(okno, 'red', (x1, y1 - 5), (x1 + 5, y1 + 5), width = 5)
    pygame.draw.line(okno, 'red', (x1 - 5, y1 + 5), (x1 + 5, y1 + 5), width = 5)

# Функция отрисовывает часы и меняет значение угла наклона стрелки
def chasiki(okno, angle, x1, y1, flag):
    # фон часов
    pygame.draw.circle(okno, 'brown', (clock_size, clock_size), clock_size)
    # вычисление координат конца стрелки
    x2 = x1 + length * math.cos(math.radians(angle))
    y2 = y1 + length * math.sin(math.radians(angle))
    # отрисовка стрелки
    pygame.draw.line(okno, 'white', (x1, y1), (x2, y2), width = 5)
    # если включена анимация, вычисляется новый угол наклона стрелки
    if flag:
        angle = (angle + 1) % 360
    # отрисовка центра часов
    pygame.draw.circle(okno, 'white', (clock_size, clock_size), 5)
    # отрисовка границы часов
    pygame.draw.circle(okno, 'white', (clock_size, clock_size), clock_size, width = 3)
    return angle

# Функция создаёт анимацию
def draw_img(okno, fon, monky, degree, cat, x1, y1, x2, y2, flag, game_clock):
    # задаётся FPS (количество кадров в секунду)
    game_clock.tick(ticki)
    # Поворот обезьянки
    monky = pygame.transform.rotate(monky, degree)
    # если анимация запущена, обезьянка вращается, круг может перемещаться
    if flag:
        degree = (degree + 3) % 360
        while ((x2 + center_kitten) == x1 and (y2 + center_kitten) == y1):
            x1, y1 = right()
    # отрисовка изображений
    okno.blit(fon, (0, 0))
    okno.blit(monky, (370, 0))
    okno.blit(cat, (x2, y2))
    # если анимация запущена, координаты обновляются
    if flag:
        x2, y2 = new_coord(x2 + center_kitten, y2 + center_kitten, x1, y1)
    return degree, x1, y1, x2, y2
    
def draw_prim(okno, x1, y1, flag, angle, x3, y3, window, running):
    # отрисовка треугольника
    treg(okno, x1, y1)
    #pygame.draw.circle(okno, 'red', (x1, y1), 10)
    angle = chasiki(okno, angle, x3, y3, flag)
    
    # обновление экрана на pygame
    pygame.display.update()
    # обновление содержимого окна на tkinter
    window.update()
    # при нажатии на крестик завершение анимации
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    return running, angle

# функция запустит координаты по кругу
##def new_coord(x, y, flag):
##    num = 500 - 25
##    new_x = x
##    new_y = y
##    if flag == 1:
##        new_y = y + 25
##        if (new_y == num):
##            flag = 2
##    elif flag == 2:
##        new_x = x + 25
##        if (new_x == num):
##            flag = 3
##    elif flag == 3:
##        new_y = y - 25
##        if (new_y == 25):
##            flag = 4
##    elif flag == 4:
##        new_x = x - 25
##        if (new_x == 25):
##            flag = 1
##    return new_x, new_y, flag
