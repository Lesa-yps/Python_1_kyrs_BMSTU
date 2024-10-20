# Талышева ИУ7-15Б
# Программа в введённой матрице символов заменяет все гласные английские буквы на
# точки и печатает матрицу до и после преобразования.

# Создаём переменную для сохранения максимальной длины элемента
leng = 0
# Ввод матрицы
n, m = map(int, input('Введите количество строк и столбцов матрицы через пробел: ').split())
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = str(input('Введите элемент матрицы строка № {0} столбец № {1}: '.format(i + 1, j + 1)))
        leng = max(len(a[i][j]), leng)
# Вывод исходной матрицы
print('Исходная матрица: ')
for i in range(n):
    print('   ', end = '')
    for j in range(m):
        print(a[i][j], end = (' ' * (leng + 3 - len(a[i][j]))))
    print()
# Проходимся по элементам матрицы и заменяем английские гласные буквы на точки
for i in range(n):
    for j in range(m):
        for k in 'euioa':
            a[i][j] = a[i][j].replace(k, '.')
# Выводим преобразованную матрицу
print('Преобразованная матрица: ')
for i in range(n):
    print('   ', end = '')
    for j in range(m):
         print(a[i][j], end = (' ' * (leng + 3 - len(a[i][j]))))
    print()
