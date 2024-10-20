# Программа переводит числа из 10 сс в 4 сс  2 кн + меню проверки на ввод нет вещ

# Импортируем библиотеки и модули
import tkinter as tk

from trans_4 import trans_4
from trans_10 import trans_10

def chooser(val):
    if val == '10 -> 4':
        res = trans_4(calc1.get())
            
        calc2.delete(0, tk.END)
        calc2.insert(0, res)
    else:
        res = trans_10(calc2.get())
            
        calc1.delete(0, tk.END)
        calc1.insert(0, res)

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"235x120+100+200")
window.title("Калькулятор")
window.resizable(0,0)

# Создаём окошко ввода и обозначаем его параметры
calc1 = tk.Entry(justify = tk.RIGHT, font = ("Calibry", 15))
calc1.grid(row = 0, column = 0, columnspan = 2, stick = 'we', padx = 5)

# Создаём окошко ввода и обозначаем его параметры
calc2 = tk.Entry(justify = tk.RIGHT, font = ("Calibry", 15))
calc2.grid(row = 1, column = 0, columnspan = 2, stick = 'we', padx = 5)

# Создаются и отображаются кнопки
tk.Button(text = '10 -> 4', bd = 7, font = ("Calibry", 13),\
                     command = lambda: chooser('10 -> 4')).grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)
tk.Button(text = '4 -> 10', bd = 7, font = ("Calibry", 13),\
                     command = lambda: chooser('4 -> 10')).grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(8):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строк
for i in range(4, 8):
    window.grid_rowconfigure(i, minsize = 60)

# Создаём меню
menu = tk.Menu(window)
window.config(menu = menu)

# Создаёт вкладку меню
menu_in = tk.Menu(menu, tearoff = 0)

menu_in.add_command(label = '10 -> 4', command = lambda: chooser('10 -> 4'))
menu_in.add_command(label = '4 -> 10', command = lambda: chooser('4 -> 10'))

menu.add_cascade(label = "Вычислить", menu = menu_in)

# Включается обработчик событий
window.mainloop()

