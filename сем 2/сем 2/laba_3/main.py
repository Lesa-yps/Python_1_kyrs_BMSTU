# Талышева Олеся ИУ7-25Б
# Программа шифрует строку в изображение и расшифровывает её

# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb
from Worker import *

# Стартовые константы
start_way = "C:/Users/Олеся/Desktop/panda.png"
start_out_way = "C:/Users/Олеся/Desktop/panda_new.png"

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"700x252+100+200")
window["bg"] = 'aqua'
window.title("Шифратор")
window.resizable(0,0)

# Создаётся строчка "Путь к исходному файлу:"
label1 = tk.Label(text="Путь к исходному файлу:", font = ("Calibry", 11))
label1.grid(row = 0, column = 0, sticky = 'w')

# Создаём окошко ввода пути и обозначаем его параметры, вставляем в него дефолтный путь
way = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
way.grid(row = 0, column = 1, columnspan = 2, stick = 'we', padx = 5)
way.insert(0, start_way)

# Создаётся строчка "Путь к зашифрованному файлу:"
label2 = tk.Label(text="Путь к зашифрованному файлу:", font = ("Calibry", 11))
label2.grid(row = 1, column = 0, sticky = 'w')

# Создаём окошко ввода пути и обозначаем его параметры, вставляем в него дефолтный путь
way_out = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
way_out.grid(row = 1, column = 1, columnspan = 2, stick = 'we', padx = 5)
way_out.insert(0, start_out_way)

# Создаётся строчка "Шифруемая строка:"
label3 = tk.Label(text="Шифруемая строка:", font = ("Calibry", 11))
label3.grid(row = 2, column = 0, sticky = 'w')

# Создаём окошко ввода строки и обозначаем его параметры
stika = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
stika.grid(row = 2, column = 1, columnspan = 2, stick = 'we', padx = 5)

# Создаётся строчка "Расшифрованная строка:"
label4 = tk.Label(text="Расшифрованная строка:", font = ("Calibry", 11))
label4.grid(row = 3, column = 0, sticky = 'w')

# Создаём окошко вывода строки и обозначаем его параметры
stika_out = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
stika_out.grid(row = 3, column = 1, columnspan = 2, stick = 'we', padx = 5)

# Создаём меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаёт вкладку меню "Действия" с выпадающим меню с действиями
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Зашифровать', command = lambda: fork('ЗАШИФРОВАТЬ', stika, stika_out, way, way_out))
menu_in.add_command(label = 'Расшифровать', command = lambda: fork('РАСШИФРОВАТЬ', stika, stika_out, way, way_out))
menu_in.add_command(label = 'Очистить шифруемую строку', command = lambda: fork('Очистить шифруемую\n строку', stika, stika_out, way, way_out))
menu_in.add_command(label = 'Очистить расшифрованную строку', command = lambda: fork('Очистить расшифрованную\n строку', stika, stika_out, way, way_out))
menu_in.add_command(label = 'Очистить исходный путь', command = lambda: fork('Очистить исходный путь', stika, stika_out, way, way_out))
menu_in.add_command(label = 'Очистить выходной путь', command = lambda: fork('Очистить выходной путь', stika, stika_out, way, way_out))

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
                     command = lambda: fork(doing, stika, stika_out, way, way_out), activebackground = "salmon", bg = "khaki")

# Создаются и отображаются кнопки
make_button('ЗАШИФРОВАТЬ').grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('РАСШИФРОВАТЬ').grid(row = 5, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить шифруемую\n строку').grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить расшифрованную\n строку').grid(row = 5, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить исходный путь').grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('Очистить выходной путь').grid(row = 5, column = 2, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(6):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строки с кнопками
for i in range(4, 6):
    window.grid_rowconfigure(i, minsize = 60)

# Включается обработчик событий
window.mainloop()
