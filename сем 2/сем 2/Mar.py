# Импортируем библиотеки и модули
import tkinter as tk
import tkinter.messagebox as mb

# Создаём окошко и обозначаем его параметры
window = tk.Tk()
window.geometry(f"235x350+100+200")
window.title("Калькулятор")

# Создаём окошко ввода и обозначаем его параметры
calc1 = tk.Entry(justify = tk.RIGHT, font = ("Calibry", 15))
calc1.grid(row = 0, column = 0, columnspan = 3, stick = 'we', padx = 5)

# Создаём окошко ввода и обозначаем его параметры
calc2 = tk.Entry(justify = tk.RIGHT, font = ("Calibry", 15))
calc2.grid(row = 1, column = 0, columnspan = 3, stick = 'we', padx = 5)

# Создаётся строчка "Ответ:"
label3 = tk.Label(text="Сумма:", font = ("Calibry", 11))
label3.grid(row = 2, column = 0, columnspan = 3, sticky = 'w')

# Создаётся строчка "Ответ:"
label4 = tk.Label(text="", font = ("Calibry", 11))
label4.grid(row = 3, column = 0, columnspan = 3, sticky = 'w')

def add_digit(digit):
    value1 = calc1.get()
    value2 = calc2.get()
    if digit == 'C1':
        calc1.delete(0, tk.END)
    elif digit == 'C2':
        calc2.delete(0, tk.END)
    elif digit == '<-1':
        calc1.delete(0, tk.END)
        calc1.insert(0, value1[:-1])
    elif digit == '<-2':
        calc2.delete(0, tk.END)
        calc2.insert(0, value2[:-1])
    elif digit == '1(1)':
        calc1.delete(0, tk.END)
        calc1.insert(0, value1 + '1')
    elif digit == '0(1)':
        calc1.delete(0, tk.END)
        calc1.insert(0, value1 + '0')
    elif digit == '1(2)':
        calc2.delete(0, tk.END)
        calc2.insert(0, value2 + '1')
    elif digit == '0(2)':
        calc2.delete(0, tk.END)
        calc2.insert(0, value2 + '0')
    elif digit == '=':
        if len(value2) > len(value1):
            value1 = '0'*(len(value2) - len(value1)) + value1
        else:
            value2 = '0'*(len(value1) - len(value2)) + value2
        summa = ''
        a = '0'
        while len(value1) > 0:
            x = int(value1[-1]) + int(value2[-1]) + int(a)
            if x >= 2:
                a = '1'
            else:
                a = '0'
            summa = str(int(x) % 2) + summa
            value1 = value1[:-1]
            value2 = value2[:-1]
        if a == '1':
            summa = '1' + summa
        label4.config(text = summa)
    

# Функция создаёт кнопку
def make_button(digit):
    return tk.Button(text = digit, bd = 7, font = ("Calibry", 13),\
                     command = lambda: add_digit(digit))

# Создаются и отображаются кнопки
make_button('C1').grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('C2').grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5, columnspan = 2)
make_button('1(1)').grid(row = 5, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('0(1)').grid(row = 5, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('1(2)').grid(row = 6, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('0(2)').grid(row = 6, column = 1, stick = 'wens', padx = 5, pady = 5, columnspan = 2)
make_button('<-1').grid(row = 7, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('<-2').grid(row = 7, column = 1, stick = 'wens', padx = 5, pady = 5, columnspan = 2)
make_button('=').grid(row = 5, column = 2, stick = 'wens', padx = 5, pady = 5)

# Задаётсяя минимальный размер колонок
for i in range(8):
    window.grid_columnconfigure(i, minsize = 60)

# Задаётсяя минимальный размер строк
for i in range(4, 8):
    window.grid_rowconfigure(i, minsize = 60)

# Включается обработчик событий
window.mainloop()
