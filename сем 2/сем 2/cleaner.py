# импортируем библиотеку
import tkinter as tk

# Функция вставит в строку вывода новое значение
def cleaner(value1, calc, value_main):
    value_main = value1
    calc.delete(0, tk.END)
    calc.insert(0, value1)
    return value_main
