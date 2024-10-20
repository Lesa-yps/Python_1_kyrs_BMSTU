# Талышева ИУ7-15Б
# Программа транспонирует матрицу

# Ввод матрицы
n = int(input('Введите количество строк матрицы: '))
a = []
for i in range(n):
    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
# Проходимся по матрице
for i in range(n):
    for j in range(i):
        # меняем элементы местами
        a[i][j], a[j][i] = a[j][i], a[i][j]
# Проверка на наличие элементов в массиве
if n <= 0:
    print('Массив пуст')
# Выводим изменённую матрицу
else:
    for i in range(n):
        print()
        print('   ', end ='')
        for j in range(n):
            print(f'{a[i][j]:^5.2f}', end = (' ' * (12 - len(f'{a[i][j]:^5.2f}'))))
        print()
        print()
