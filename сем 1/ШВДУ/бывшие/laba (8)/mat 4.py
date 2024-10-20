# Талышева ИУ7-15Б
# Программа находит строку в введенной матрице с наименьшим количеством чётных элементов

n = int(input('Введите количество строк матрицы: '))
a = []
for i in range(n):
    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
ind_ma = ind_mi = None
smi = sma = 0
for i in range(len(a[0])):
    smi += sum(a[0])
    sma += sum(a[0])
for i in range(len(a[0])):
    count = 0
    for j in range(n):
        count += a[j][i]
    if count < smi:
        smi = count
        ind_mi = i
    if count > sma:
        sma = count
        ind_ma = i
for i in range(n):
    a[i][ind_ma], a[i][ind_mi] = a[i][ind_mi], a[i][ind_ma]
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
