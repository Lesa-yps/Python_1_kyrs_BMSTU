# Талышева Олеся ИУ7-25Б
# Программа шифрует строку в изображение и расшифровывает её

# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb
from Worker import *
from Check import is_tilda

# Константы
start_way = "C:/Users/Олеся/Desktop/panda.png"
start_out_way = "C:/Users/Олеся/Desktop/panda_new.png"

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"900x145+100+200")
window["bg"] = 'aqua'
window.title("Шифратор")
window.resizable(0,0)

# Создаётся строчка "Путь к файлу:"
label1 = tk.Label(text="Путь к старт-файлу:", font = ("Calibry", 11))
label1.grid(row = 0, column = 0, sticky = 'w')

# Создаём окошко ввода пути и обозначаем его параметры, вставляем в него дефолтный путь
way = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
way.grid(row = 0, column = 1, columnspan = 4, stick = 'we', padx = 5)
way.insert(0, start_way)

# Создаётся строчка "Путь к файлу:"
label2 = tk.Label(text="Путь к финиш-файлу:", font = ("Calibry", 11))
label2.grid(row = 1, column = 0, sticky = 'w')

# Создаём окошко ввода пути и обозначаем его параметры, вставляем в него дефолтный путь
way_out = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
way_out.grid(row = 1, column = 1, columnspan = 4, stick = 'we', padx = 5)
way_out.insert(0, start_out_way)

# Создаётся строчка "Строка:"
label2 = tk.Label(text="Строка:", font = ("Calibry", 11))
label2.grid(row = 2, column = 0, sticky = 'w')

# Создаём окошко ввода строки и обозначаем его параметры
stika = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
stika.grid(row = 2, column = 1, columnspan = 4, stick = 'we', padx = 5)

# Создаём меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаёт вкладку меню "Действия" с выпадающим меню с действиями
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Зашифровать', command = lambda: fork('ЗАШИФРОВАТЬ', stika, way, way_out))
menu_in.add_command(label = 'Расшифровать', command = lambda: fork('РАСШИФРОВАТЬ', stika, way, way_out))
menu_in.add_command(label = 'Очистить строчку', command = lambda: fork('Очистить строку', stika, way, way_out))
menu_in.add_command(label = 'Очистить старт-путь', command = lambda: fork('Очистить старт-путь', stika, way, way_out))
menu_in.add_command(label = 'Очистить финиш-путь', command = lambda: fork('Очистить финиш-путь', stika, way, way_out))

menu.add_cascade(label = "Действия", menu = menu_in)


# Создаёт вкладку меню "Информация" с выпадающим меню с информацией об авторе и программе
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Программа шифрует строку в изображение и расшифровывает её"))

menu.add_cascade(label = "Информация", menu = menu_inf)


# Функция создаёт кнопку
def make_button(doing):
    return tk.Button(text = doing, bd = 7, font = ("Calibry", 13),\
                     command = lambda: fork(doing, stika, way, way_out), activebackground = "salmon", bg = "khaki")

# Создаются и отображаются кнопки
make_button('ЗАШИФРОВАТЬ').grid(row = 3, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('РАСШИФРОВАТЬ').grid(row = 3, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить строку').grid(row = 3, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить старт-путь').grid(row = 3, column = 3, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить финиш-путь').grid(row = 3, column = 4, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(5):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строк
window.grid_rowconfigure(3, minsize = 60)

# Реагирует на нажатие клавиш и вызывает функцию checker
window.bind('<Key>', lambda key: is_tilda(key, stika))

# Включается обработчик событий
window.mainloop()
