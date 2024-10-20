import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя игра")

# Основной игровой цикл
running = True
while running:

    # Отрисовка на экране (замените этот блок своим кодом отрисовки)
    window.fill((255, 255, 255)) # (255, 255, 255) == 'white'
    pygame.draw.circle(window, 'pink', (400, 300), 200)
    pygame.draw.rect(window, 'yellow', [255, 43, 400, 300], 5) # прибавляет
    pygame.draw.ellipse(window, 'red', (123, 213, 76, 132), 3) # прибавляет
    pygame.draw.polygon(window, 'blue', [(155, 50), (400, 300), (23, 120), (340, 210)], 3) # координаты

    # Обновление экрана
    pygame.display.update()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение Pygame
pygame.quit()
