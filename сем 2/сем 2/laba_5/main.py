# Талышева Олеся ИУ7-25Б
# создание анимации

# импортируем библиотеки
import os
import tkinter as tk
import tkinter.messagebox as mb
import pygame
from random import randint
from logic import *

# константы
white = (255, 255, 255)
size_py = 500

# создает объект Clock, который помогает контролировать скорость анимации в приложении на pygame
game_clock = pygame.time.Clock()

# cоздается графическое окно Tk() с некоторыми параметрами
window = tk.Tk()
window.geometry(f"500x570+100+200")
window["bg"] = 'light blue'
window.title("Анимация")
window.resizable(0,0)

# Создаются два фрейма: framik для отображения анимации на pygame и but_framik для отображения кнопок
framik = tk.Frame(window, width = size_py, height = size_py)
framik.grid(columnspan = size_py, rowspan = size_py)
framik.pack(side = 'top')

but_framik = tk.Frame(window, width = size_py, height = 70)
but_framik.pack(side = 'bottom')

# Функция меняет значение флага для запуска/остановки анимации
def fix(what):
    global flag
    flag = what

# Создается меню с двумя вкладками: "Действия" и "Информация"
menu = tk.Menu(window) 
window.config(menu = menu)

# Вкладка "Действия" содержит выпадающее меню с командами "GO" и "STOP"
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'GO', command = lambda: fix(True))
menu_in.add_command(label = 'STOP', command = lambda: fix(False))

menu.add_cascade(label = "Действия", menu = menu_in)


# вкладка "Информация" содержит выпадающее меню с информацией об авторе и программе
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Анимация: котик догоняет красную точку, обезьянка вращается, часы идут."))

menu.add_cascade(label = "Информация", menu = menu_inf)

# Создаются две кнопки: "GO" и "STOP"
button_go = tk.Button(but_framik, text='GO', command=lambda: fix(True), width=33, height=3, activebackground = "salmon", bg = "khaki")
button_go.pack(side='left', padx=5, pady=5)
button_stop = tk.Button(but_framik, text='STOP', command=lambda: fix(False), width=33, height=3, activebackground = "salmon", bg = "khaki")
button_stop.pack(side='left')

# Модуль os - позиция окна
os.environ['SDL_WINDOWID'] = str(framik.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

# Инициализация PyGame
pygame.init()
# Окно игры: размер, позиция
okno = pygame.display.set_mode([size_py, size_py])
# pygame.display.set_caption("Sky")
# okno.fill((255, 255, 255))

##box = pygame.Surface((20, 20))
##box.fill('red')

# Задаются начальные координаты объектов
x1, y1 = right()
x2, y2 = right()

# Задаются начальные значения флажков
running = flag = True

# координаты центра часов
x3, y3 = 40, 40
# угол поворота стрелки в градусах
angle = 0  

# подгрузка изображений
fon = pygame.image.load('paint/pole.jpg')
monky = pygame.image.load('paint/monki.jpg')#.convert()
cat = pygame.image.load('paint/cat.jpg')

# масштабирование изображений
fon = pygame.transform.scale(fon, (600, 600))
monky = pygame.transform.scale(monky, (100, 100))
cat = pygame.transform.scale(cat, (100, 100))

# Убирается фон
monky.set_colorkey(white)
cat.set_colorkey(white)

# переменная для поворота обезьянки
degree = 0

# Запускается анимация на pygame с помощью цикла while.
# В цикле вызывается функция draw(), которая отрисовывает анимацию на pygame
while running:
    degree, x1, y1, x2, y2 = draw_img(okno, fon, monky, degree, cat, x1, y1, x2, y2, flag, game_clock)
    running, angle = draw_prim(okno, x1, y1, flag, angle, x3, y3, window, running)
    
# обновляет содержимое окна на экране
pygame.display.flip()

# Включается обработчик событий
window.mainloop()


 
