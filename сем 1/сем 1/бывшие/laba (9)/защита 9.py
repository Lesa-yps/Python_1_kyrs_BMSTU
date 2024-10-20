# Талышева ИУ7-15Б
# Программа поворачивает квадратную целочисленную матрицу на 180 градусов

from math import ceil
n = int(input('Введите количество строк матрицы: '))
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input('Введите элемент в строке № {0} столбце № {1}: '.format(i + 1, j + 1)))

for i in range(ceil(n / 2)):
    for j in range(n):
        if n % 2 == 1 and i == ceil(n / 2) - 1 and j == round(n / 2) - 1:
            break
        else:
            a[i][j], a[n - i - 1][n - j -1] = a[n - i - 1][n - j -1], a[i][j]

print('Итоговая матрица: ')
for i in range(n):
    print('   ', end = '')
    for j in range(n):
        print(f'{a[i][j]:<7d}', end = (' ' * (8 - len(f'{a[i][j]:<7d}'))))
    print()

