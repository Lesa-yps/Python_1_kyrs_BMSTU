from stefan import *
from change import *

import numpy as np
import math as m

E = 1e-6

# Вычисляет значение введённой функции
def f(x):
    fx = "m.sin(x)"
    fx = fx.replace("^", "**")
    new_fx = fx[:3]
    new_fx = changer(new_fx)
    for i in fx[3:]:
        new_fx += i
        new_fx = changer(new_fx)
    return eval(new_fx)

a = -10
b = 10
h = 2
eps = 0.001
N_max = 10


k = 1
# переменная показывает был ли корень, лежащий на границе отрезка, уже исследован
gran = 0
# проверка существования корня на отрезке
while (h > 0 and a <= b) or (h < 0 and a >= b):

            # Проверка существования корня на отрезке
            x_poi = np.linspace(a, a + h, int(abs(h) * 1100))
            y_poi = np.array([f(j) for j in x_poi])
            
            mask = np.abs(y_poi) < 1e-3

            # Если корень есть на отрезке и он не поторяющийся
            if True in mask and gran == 0:
                if abs(f(a + h)) < E:
                    gran = 1
                # переменная содержит код ошибки
                cod = 0
                # вызывается функция, реализующая метод Стефансона для уточнения корней с проверкой на ошибки
                try:
                    xk, n, flag = Stef(a, a + h, eps, N_max, f)
                # при делении на нуль в таблицу выводится код ошибки 3
                except ZeroDivisionError:
                    print(str(k), '[ {:^7.2f}; {:^7.2f} ]'.format(a, a + h), '-', '-', '-', '3')
                # при других ошибках в таблицу выводится код ошибки 4
                except Exception:
                    print(str(k), '[ {:^7.2f}; {:^7.2f} ]'.format(a, a + h), '-', '-', '-', '4')
                else:
                    # при достижении максимального количества итераций при недостаточной точности в таблицу выводится код ошибки 2
                    if flag: cod = 2
                    # вывод строки таблицы
                    print(str(k), '[ {:^7.2f}; {:^7.2f} ]'.format(a, a + h), '{:^7.2f}'.format(xk), '{:^7.2f}'.format(f(xk)), str(n), str(cod))
                # увеличение номера корня
                k += 1
            else:
                # если на этом отрезке не было корня, отрезок смещается
                gran = 0
            a += h
