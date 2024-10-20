# Талышева ИУ7-15Б
# Программа формирует матрицу C путём построчного перемножения введённых матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом складывает все
# элементы в столбцах матрицы C и записывает их в массив V. Печатает матрицы A, B, C и массив V

# Ввод матриц A и B
n = int(input('Введите количество строк матриц: '))
a = []
for i in range(n):
    a.append([float(c) for c in input('Введите элементы строки № {} матрицы A через пробел: '.format(i + 1)).split()])
b = []
for i in range(n):
    b.append([float(c) for c in input('Введите элементы строки № {} матрицы B через пробел: '.format(i + 1)).split()])
    while len(a[i]) != len(b[i]):
        print('Матрицы должны быть одинаковой размерности. Повторите попытку.')
        b.append([float(c) for c in input('Введите элементы строки № {} матрицы B через пробел: '.format(i + 1)).split()])
# Вывод матриц А и В
print('Исходная матрица А: ')
for i in range(n):
    print('   ', end = '')
    for j in range(len(a[i])):
        print(f'{a[i][j]:<5.2f}', end = (' ' * (8 - len(f'{a[i][j]:<5.2f}'))))
    print()
print('Исходная матрица B: ')
for i in range(n):
    print('   ', end = '')
    for j in range(len(b[i])):
        print(f'{b[i][j]:<5.2f}', end = (' ' * (8 - len(f'{b[i][j]:<5.2f}'))))
    print()
# Проходимся по элементам матриц А и В и формируем матрицу С,
# перемножая соответствующие элементы матриц
c = [[0] * len(a[0]) for i in range(n)]
for i in range(n):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] * b[i][j]
# Формируем массив V, складывая элементы матрицы С по столбцам
v = [0] * len(c[0])
for i in range(len(c[0])):
    for j in range(n):
        v[i] += c[j][i]
# Выводим матрицу C и массив V
print('Полученная матрица С: ')
for i in range(n):
    print('   ', end = '')
    for j in range(len(c[0])):
         print(f'{c[i][j]:<5.2f}', end = (' ' * (8 - len(f'{c[i][j]:<5.2f}'))))
    print()
print('Массив V: ')
print(*v)
