# импортируем библиотеки
import math as m
import tkinter as tk
import pygame

#константы
rad = 60
len_line = 50
y_main = 250
count_line = 6
size_py = 500
weight_line = 4
size_part_sun = rad + len_line
change_x = 8
change_angle = 8



def lop(okno, x_main, angle, flag):
    # отрисовка лучиков
    for i in range(count_line):
        x1 = x_main + m.sin(m.radians(angle + i * (360 // count_line))) * (rad - 10)
        y1 = y_main - m.cos(m.radians(angle + i * (360 // count_line))) * (rad - 10)
        x2 = x_main + m.sin(m.radians(angle + i * (360 // count_line))) * (rad + len_line)
        y2 = y_main - m.cos(m.radians(angle + i * (360 // count_line))) * (rad + len_line)
        pygame.draw.line(okno, 'yellow', [x1, y1], [x2, y2], weight_line)
    # изменение angle для вращения
    if flag:
        angle = (angle + change_angle) % 360 
    return angle



# Функция создаёт анимацию
def draw_img(okno, flag, game_clock, x_main, angle):
    # задаётся FPS (количество кадров в секунду)
    game_clock.tick(20)
    # фон
    pygame.draw.rect(okno, 'light blue', (0, 0, size_py, size_py))
    # солнце
    pygame.draw.circle(okno, 'yellow', (x_main, y_main), rad)
    # отрисовка лучиков и изменение угла
    angle = lop(okno, x_main, angle, flag)
    # если анимация запущена, координаты х_main обновляются
    if flag:
        x_main += change_x
    # если дошли до конца полотна, координаты х_main становятся начальными
    if flag and (x_main > size_py + size_part_sun):
        x_main = - size_part_sun
    return angle, x_main



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
