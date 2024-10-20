# Талышева ИУ7-15Б
# Программа находит строку в введенной матрице с наименьшим количеством чётных элементов

n = int(input('Введите количество строк матрицы: '))
a = []
for i in range(n):
    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
ind_mi = ind_ma = None
cmi = len(a[0]) + 1
cma = -1
for i in range(n):
    count = 0
    for j in range(len(a[i])):
        if a[i][j] < 0:
            count += 1
    if count < cmi:
        cmi = count
        ind_mi = i
    if count > cma:
        cma = count
        ind_ma = i
a[ind_mi], a[ind_ma] = a[ind_ma], a[ind_mi]
if n <= 0:
    print('Массив пуст')
else:
    for i in range(n):
        print()
        print('   ', end ='')
        for j in range(len(a[i])):
            print(f'{a[i][j]:^5.2f}', end = (' ' * (12 - len(f'{a[i][j]:^5.2f}'))))
        print()
        print()
