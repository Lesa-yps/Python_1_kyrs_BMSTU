#Талышева ИУ7-25Б

# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb

from Mader import made

# Стартовые константы
start_way = "C:/Users/Олеся/Desktop/panda.png"
start_out_way = "C:/Users/Олеся/Desktop/panda_new.png"

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"630x150+100+200")
window["bg"] = 'light green'
window.title("Плюс")
window.resizable(0,0)

# Создаётся строчка "Путь к исходному файлу:"
label1 = tk.Label(text="Путь к исходному файлу:", font = ("Calibry", 11))
label1.grid(row = 0, column = 0, sticky = 'w')

# Создаём окошко ввода пути и обозначаем его параметры, вставляем в него дефолтный путь
way = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
way.grid(row = 0, column = 1, columnspan = 4, stick = 'we', padx = 5)
way.insert(0, start_way)

# Создаётся строчка "Путь к изменённому файлу:"
label2 = tk.Label(text="Путь к изменённому файлу:", font = ("Calibry", 11))
label2.grid(row = 1, column = 0, sticky = 'w')

# Создаём окошко ввода пути и обозначаем его параметры, вставляем в него дефолтный путь
way_out = tk.Entry(justify = tk.LEFT, font = ("Calibry", 15))
way_out.grid(row = 1, column = 1, columnspan = 4, stick = 'we', padx = 5)
way_out.insert(0, start_out_way)

# Создаём меню
menu = tk.Menu(window) 
window.config(menu = menu)

# Создаёт вкладку меню "Действия" с выпадающим меню с действиями
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = 'Изменить изображение', command = lambda: made('Изменить\nизображение', way, way_out))
menu_in.add_command(label = 'Вывести начальное изображение', command = lambda: made('Вывести\nначальное\nизображение', way, way_out))
menu_in.add_command(label = 'Вывести изменённое изображение', command = lambda: made('Вывести\nизменённое\nизображение', way, way_out))

menu.add_cascade(label = "Действия", menu = menu_in)


# Создаёт вкладку меню "Информация" с выпадающим меню с информацией об авторе и программе
menu_inf = tk.Menu(menu, tearoff = 0)

menu_inf.add_command(label = 'Информация об авторе', command = lambda: mb.showinfo('Информация об авторе', \
                                                                                   "автор - Талышева ИУ7-25Б"))
menu_inf.add_command(label = 'Информация о программе', command = lambda: mb.showinfo('Информация о программе',\
                                                                                     "Программа перекрывает изображение видимым красным плюсом"))

menu.add_cascade(label = "Информация", menu = menu_inf)


# Функция создаёт кнопку
def make_button(doing):
    return tk.Button(text = doing, bd = 7, font = ("Calibry", 13),\
                     command = lambda: made(doing, way, way_out), activebackground = "salmon", bg = "khaki")

# Создаются и отображаются кнопки
make_button('Изменить\nизображение').grid(row = 4, column = 0, stick = 'wens', columnspan = 2, padx = 5, pady = 5)
make_button('Вывести\nначальное\nизображение').grid(row = 4, column = 2, stick = 'wens', columnspan = 2, padx = 5, pady = 5)
make_button('Вывести\nизменённое\nизображение').grid(row = 4, column = 4, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(5):
    window.grid_columnconfigure(i, minsize = 100)

# Задаётсяя минимальный размер строки с кнопками
window.grid_rowconfigure(4, minsize = 60)

# Включается обработчик событий
window.mainloop()
