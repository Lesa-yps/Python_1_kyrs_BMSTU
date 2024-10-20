'''
прямоугольники
pygame.draw.rect(sc, (255, 255, 255), 
                 (20, 20, 100, 75))
pygame.draw.rect(sc, (64, 128, 255), 
                 (150, 20, 100, 75), 8)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
 
r1 = pygame.Rect((150, 20, 100, 75))
 
pygame.draw.rect(sc, WHITE, (20, 20, 100, 75))
pygame.draw.rect(sc, LIGHT_BLUE, r1, 8)

линии
pygame.draw.line(sc, WHITE, 
                 [10, 30], 
                 [290, 15], 3)
pygame.draw.line(sc, WHITE, 
                 [10, 50], 
                 [290, 35])
pygame.draw.aaline(sc, WHITE, 
                   [10, 70], 
                   [290, 55])

ломаные линии
pygame.draw.lines(sc, WHITE, True,
                  [[10, 10], [140, 70],
                   [280, 20]], 2)
pygame.draw.aalines(sc, WHITE, False,
                    [[10, 100], [140, 170],
                     [280, 110]])

Функция polygon() рисует произвольный многоугольник. Задаются координаты вершин.

pygame.draw.polygon(sc, WHITE, 
                    [[150, 10], [180, 50], 
                     [90, 90], [30, 30]])
pygame.draw.polygon(sc, WHITE, 
                    [[250, 110], [280, 150], 
                     [190, 190], [130, 130]])
pygame.draw.aalines(sc, WHITE, True, 
                    [[250, 110], [280, 150], 
                     [190, 190], [130, 130]])

Функция circle() рисует круги. Указывается центр окружности и радиус:

pygame.draw.circle(sc, YELLOW, 
                   (100, 100), 50)
pygame.draw.circle(sc, PINK, 
                   (200, 100), 50, 10)

В случае эллипса передается описывающая его прямоугольная область:

pygame.draw.ellipse(sc, GREEN, 
                    (10, 50, 280, 100))

Наконец, дуга:

pi = 3.14
pygame.draw.arc(sc, WHITE,
                (10, 50, 280, 100),
                0, pi)
pygame.draw.arc(sc, PINK,
                (50, 30, 200, 150),
                pi, 2*pi, 3)
'''

# здесь подключаются модули
import pygame
import sys
 
# здесь определяются константы,
# классы и функции
FPS = 60
 
# здесь происходит инициация,
# создание объектов
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()
 
# главный цикл
while True:
 
    # задержка
    clock.tick(FPS)
 
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
 
    # обновление экрана
    pygame.display.update()
