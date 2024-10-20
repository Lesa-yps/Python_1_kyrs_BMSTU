# Талышева ИУ7-15Б
# Программа находит строку в введенной матрице с наименьшим количеством чётных элементов

# Ввод матрицы
##n = int(input('Введите количество строк матрицы: '))
##a = []
##for i in range(n):
##    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
# Задаём переменную для сохранения индекса строки и минимального количества чётных элементов в строке
a = [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]
n = 4
i = 0
for i in range(n):
        print('   ', end = '')
        for j in range(n):
            print(f'{a[i][j]:^5.2f}', end = (' ' * (12 - len(f'{a[i][j]:^5.2f}'))))
        print()
# Проходимся по матрице
for i in range(round(n // 2)):
    print(i)
    # задаём счётчик количества чётных элементов в строке
    for j in range(i, n - i - 1):
        print(i, j)
        print(a[i][j], '->', a[j][n - i - 1], '->', a[n - i - 1][n - j - 1], '->', a[n - i - 1][n - j - 1])
        a[j][n - i - 1], a[n - i - 1][n - j - 1], a[j][n - i - 1], a[i][j] = a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - i - 1][n - j - 1]
##        a[i][j], a[j][n - i - 1], a[n - j - 1][n - j - 1], a[n - j - 1][j] = a[j][n - i - 1], a[n - j - 1][n - j - 1], a[n - j - 1][j], a[i][j]
        print('Change')
        for c in range(n):
            print('   ', end = '')
            for d in range(n):
                print(f'{a[c][d]:^5.2f}', end = (' ' * (12 - len(f'{a[c][d]:^5.2f}'))))
            print()
# Проверка на наличие элементов в массиве
if n <= 0:
    print('Массив пуст')
# Выводим искомую строку
else:
    print('New matrix')
    for i in range(n):
        print('   ', end = '')
        for j in range(n):
            print(f'{a[i][j]:^5.2f}', end = (' ' * (12 - len(f'{a[i][j]:^5.2f}'))))
        print()
