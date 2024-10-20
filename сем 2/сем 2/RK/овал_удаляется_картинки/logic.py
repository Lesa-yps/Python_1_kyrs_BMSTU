# импортируем библиотеки
import math
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

# Функция создаёт анимацию
def draw_img(okno, fon, house, x, y, size_x, size_y, flag, game_clock, window, running):
    # задаётся FPS (количество кадров в секунду)
    game_clock.tick(20)
    # отрисовка изображений
    okno.blit(fon, (0, 0))
    okno.blit(house, (360, 230))
    # если анимация запущена, координаты обновляются
    if flag:
        x, y, size_x, size_y = new_coord(x, y, size_x, size_y)
    pygame.draw.ellipse(okno, 'red', (x, y, size_x, size_y))
    #pygame.draw.rect(okno, 'blue', (x, y, size_x, size_y), 3)
    #pygame.draw.rect(okno, 'green', (0, 0, 500, 500), 4)
    # обновление экрана на pygame
    pygame.display.update()
    # обновление содержимого окна на tkinter
    window.update()
    # при нажатии на крестик завершение анимации
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    return running, x, y, size_x, size_y
