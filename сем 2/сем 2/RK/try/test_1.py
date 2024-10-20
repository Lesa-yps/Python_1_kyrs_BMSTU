import pygame
import tkinter as tk
import os

screen = tk.Tk()
screen.geometry(f"700x700+100+100")
screen["bg"] = 'blue'
screen.title("My ALL")
screen.resizable(0, 0)

framik_p = tk.Frame(screen, height = 500, width = 500)
framik_p.grid(columnspan = 500, rowspan = 500)
framik_p.pack()

framik = tk.Frame(screen, height = 200, width = 700)
framik.pack(side = "top")

# Модуль os - позиция окна
os.environ['SDL_WINDOWID'] = str(framik_p.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

game_clock = pygame.time.Clock()

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My Game")


flag = True
while flag:

    game_clock.tick(25)

    window.fill("green")

    pygame.draw.rect(window, 'red', (123, 121, 190, 100), 2)

    pygame.display.update()
    screen.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

# обновляет содержимое окна на экране
pygame.display.flip()

# Включается обработчик событий
screen.mainloop()
