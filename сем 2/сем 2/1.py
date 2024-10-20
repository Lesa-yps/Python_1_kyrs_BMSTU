# программа выполняет сложение и вычитание вещественных чисел в 4-й системе счисления
# Лабораторная работа No 1 "Калькулятор систем счисления"
# приложение использует модуль создания оконных приложений Tkinter, реализующее индивидуальное задание.
# Интерфейс предоставляет ввод символов: как числовых, так и знаков
# операций - и с использованием клавиатуры, и с помощью кнопок приложения.
# Также в приложении создано меню, в котором есть следующие пункты:
# ● заданные действия,
# ● очистка полей ввода/вывода (по одному и всех сразу),
# ● информация о программе и авторе.

import tkinter as tk

window = tk.Tk()

##border_effects = {
##    "сложить числа": tk.FLAT,
##    "вычесть числа": tk.SUNKEN,
##    "очистить поле": tk.RAISED,
##    "удалить последний знак": tk.GROOVE
##}
##
##for relief_name, relief in border_effects.items():
##    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
##    frame.pack(side=tk.TOP)
##    label = tk.Label(master=frame, text=relief_name)
##    label.pack()

frame1 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame1.pack(side=tk.LEFT)
label1 = tk.Label(master=frame1, text="автор - Талышева ИУ7-25Б")
label1.pack()


frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame2.pack(side=tk.LEFT)
label2 = tk.Label(master=frame2, text="приложение выполняет сложение и вычитание вещественных чисел в 4-й системе счисления")
label2.pack()

hint = tk.Label(text = "Введите выражение, которое нужно вычислить в 4-й системе счисления")
hint.pack()

text_from_user = tk.Entry()
text_from_user.pack()

button = tk.Button(text = "=", bg = "green", width = 3, height = 1)
button.pack()

hint = tk.Label(text = "Ошибки:")
hint.pack()

error = tk.Entry()
error.pack()


digit = text_from_user.get()
print(digit)

# Удалит последний символ
text_from_user.delete(-1)

# Очистит поле ввода
text_from_user.delete(0, tk.END)

error.delete(0, tk.END)
error.insert(0, "Ошибка такая-то")





# Запускает обработчик событий
window.mainloop()


n = 0
result = 0
while n != "=":
    n = str(input("Ведите что-то-там: "))
    try:
        n = float(n)
    except ValueError:
        if n == "+":
            
            






