# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb
from Maker_line import make_line

# Функция обновляет предполагаемую на построение прямую (коордиаты 2 точек, по которым она построится)
# и максимальное значение count (если нужно)
def check_count(count, max_count, i, j, max_i, max_j):
    if (count > max_count):
        max_count = count
        max_i = i
        max_j = j
    return max_count, max_i, max_j

# Из массива выделяются исходные координаты точки
def made_pounts(first, second):
    x1 = (first[0] + first[2]) // 2
    y1 = (first[1] + first[3]) // 2
    x2 = (second[0] + second[2]) // 2
    y2 = (second[1] + second[3]) // 2
    return x1, x2, y1, y2

# Создаётся список координат по тэгу
def made_list_coord(cnv, sth):
    listic = cnv.find_withtag(sth)
    res = []
    for i in listic:
        res.append(cnv.coords(i))
    return res

# Функция определяет 2 точки, поведённная через которые прямая параллельна максимальному количеству существующих прямых,
# и отрисовывет прямую по этим точкам
def brain(cnv, x1_win, x2_win, y1_win, y2_win):
    # Создаются списки координат точек и линий по тэгу и проверяются на пустоту
    tochka = made_list_coord(cnv, 'A')
    if len(tochka) == 0:
        mb.showerror('Ошибка!', "Точки отсутствуют.")
        return 1
    line = made_list_coord(cnv, 'B')
    if len(line) == 0:
        mb.showerror('Ошибка!', "Линии отсутствуют.")
        return 1
    max_count = 0
    max_i = 0
    max_j = 0
    # Определяются 2 точки, поведённная через которые прямая параллельна максимальному количеству существующих прямых,
    for i in range(len(tochka)):
        for j in range(i + 1, len(tochka)):
            count = 0
            x1, x2, y1, y2 = made_pounts(tochka[i], tochka[j])
            if (x1 == x2):
                for k in line:
                    if k[0] == k[2]:
                        count += 1
                max_count, max_i, max_j = check_count(count, max_count, i, j, max_i, max_j)
            else:
                check = (y2 - y1) / (x2 - x1)
                for k in line:
                    if k[0] == k[2]:
                        continue
                    if ((k[3] - k[1]) / (k[2] - k[0])) == check:
                        count += 1
                max_count, max_i, max_j = check_count(count, max_count, i, j, max_i, max_j)
    # Отрисовка прямой с проверкой на её существование 
    if max_count == 0:
        mb.showwarning('Предупреждение', "Отсутствуют точки, чтобы прямая, проведённая через них, была параллельна хотя бы 1 существующей прямой")
    else:
        x1, x2, y1, y2 = made_pounts(tochka[max_i], tochka[max_j])
        make_line(cnv, x1, x2, y1, y2, "blue")
