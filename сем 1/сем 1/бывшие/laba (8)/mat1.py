# Талышева ИУ7-15Б
# Программа находит строку в введенной матрице с наименьшим количеством чётных элементов

n = int(input('Введите количество строк матрицы: '))
a = []
for i in range(n):
    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
ind = None
cm = len(a[0]) + 1
for i in range(n):
    count = 0
    for j in range(len(a[i])):
        if a[i][j] % 2 == 0:
            count += 1
    if count < cm:
        cm = count
        ind = i
if n <= 0:
    print('Массив пуст')
else:
    for j in range(len(a[ind])):
        print(f'{a[ind][j]:^5.2f}', end = (' ' * (12 - len(f'{a[ind][j]:^5.2f}'))))
