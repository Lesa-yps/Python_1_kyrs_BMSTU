# импортируем библиотеки
import math as m
import tkinter as tk
import pygame

rad = 25

def lop(okno, x, y, angle, degrees, flag, sth):

    y -= 80

    # применение поворота
    x1 = x + m.sin(m.radians(angle)) * rad
    y1 = y + m.cos(m.radians(angle)) * rad
    x2 = x + m.sin(m.radians(angle + 90)) * rad
    y2 = y + m.cos(m.radians(angle + 90)) * rad
    x3 = x + m.sin(m.radians(angle + 180)) * rad
    y3 = y + m.cos(m.radians(angle + 180)) * rad
    x4 = x + m.sin(m.radians(angle + 270)) * rad
    y4 = y + m.cos(m.radians(angle + 270)) * rad

    pygame.draw.line(okno, 'black', [x1, y1], [x3, y3], 3)
    pygame.draw.line(okno, 'black', [x2, y2], [x4, y4], 3)
    
    # изменение переменных angle и degrees для передвижения
    if flag:
        angle = (angle + 10) % 360
        degrees = (degrees + 10) % 360
        sth += 1
        
    return angle, degrees, sth

# отрисовка вертолёта
def plane(x_main, y_main, okno):
    pygame.draw.rect(okno, 'light green', (0, 0, 500, 500))
    
    pygame.draw.line(okno, 'black', [x_main - 20, y_main + 40], [x_main - 20, y_main + 80], 3)
    pygame.draw.line(okno, 'black', [x_main + 20, y_main + 40], [x_main + 20, y_main + 80], 3)
    pygame.draw.lines(okno, 'black', False, [[x_main - 100, y_main + 50], [x_main - 100, y_main + 80], [x_main + 90,y_main + 80]], 2)
    pygame.draw.line(okno, 'black', [x_main, y_main - 50], [x_main, y_main - 80], 3)
    
    pygame.draw.ellipse(okno, 'blue', (x_main - 100, y_main - 50, 200, 100))
    pygame.draw.rect(okno, 'pink', (x_main - 50, y_main - 25, 25, 25))

# Функция создаёт анимацию
def draw_img(okno, flag, game_clock, x_main, y_main, angle, degrees, sth):
    # задаётся FPS (количество кадров в секунду)
    game_clock.tick(20)
    # если анимация запущена, координаты обновляются

    x_main = m.sin(m.radians(degrees)) * 50 + 250
    if flag:
        y_main -= sth

    plane(x_main, y_main, okno)

    angle, degrees, sth = lop(okno, x_main, y_main, angle, degrees, flag, sth)

    if flag and (y_main + 80) < 0:
        sth = 0
        y_main = 605
        x_main = 250
    return angle, degrees, sth, x_main, y_main

def draw_img2(window, running):
    # обновление экрана на pygame
    pygame.display.update()
    # обновление содержимого окна на tkinter
    window.update()
    # при нажатии на крестик завершение анимации
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    return running
