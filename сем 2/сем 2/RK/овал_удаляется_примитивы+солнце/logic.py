# импортируем библиотеки
import math as m
import tkinter as tk
import pygame
from random import randint

def new_coord(x, y, size_x, size_y):
    x = x + 10
    y = - x + 500
    size_x -= 2
    size_y -= 1
    if x > 500 or size_x <= 0 or size_y <= 0:
        x, y = 50, 450
        size_x, size_y = 80, 40
    return x, y, size_x, size_y

def house(x, y, size, okno):
    pygame.draw.rect(okno, 'brown', (x + size // 20, y + size // 3 - 1, size - (size // 20) * 2, size))
    pygame.draw.polygon(okno, 'pink', [(x + size // 2, y), (x, y + size // 3 + 1), (x + size, y + size // 3 + 1)])

x_main = y_main = lena = 50

def make(angle, okno, adder):
    y = y_main + lena * m.cos(angle + adder)
    x = x_main + lena * m.sin(angle + adder)
    pygame.draw.line(okno, 'yellow', [x, y], [2 * x, 2 * y], 5)
    
def oblako(angle, flag, okno):
    pygame.draw.circle(okno, 'yellow', (x_main, y_main), lena)
    for adder in range(0, 50, 10):
        make(angle, okno, adder)
    
    if flag:
        angle = (angle + 1) % 360
    return angle

# Функция создаёт анимацию
def draw_img(okno, x, y, size_x, size_y, flag, game_clock, window, running, angle):
    # задаётся FPS (количество кадров в секунду)
    game_clock.tick(20)
    # отрисовка изображений
    pygame.draw.rect(okno, 'light blue', (0, 0, 500, 500))
    pygame.draw.rect(okno, 'green', (0, 480, 500, 480))
    pygame.draw.polygon(okno, 'green', [[250, 480], [280, 460], [460, 460], [500, 480]])
    house(280, 230, 180, okno)
    angle = oblako(angle, flag, okno)
    # если анимация запущена, координаты обновляются
    if flag:
        x, y, size_x, size_y = new_coord(x, y, size_x, size_y)
    pygame.draw.ellipse(okno, 'red', (x, y, size_x, size_y))
    #pygame.draw.rect(okno, 'green', (x, y, size_x, size_y), 3)
    # обновление экрана на pygame
    pygame.display.update()
    # обновление содержимого окна на tkinter
    window.update()
    # при нажатии на крестик завершение анимации
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    return running, x, y, size_x, size_y, angle
