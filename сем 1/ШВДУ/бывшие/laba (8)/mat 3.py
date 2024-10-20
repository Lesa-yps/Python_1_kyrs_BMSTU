# Талышева ИУ7-15Б
# Программа находит строку в введенной матрице с наименьшим количеством чётных элементов

n = int(input('Введите количество строк матрицы: '))
a = []
for i in range(n):
    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
ind = None
flag = False
cm = len(a[0]) + 1
for i in range(len(a[0])):
    count = 0
    for j in range(n):
        x = a[j][i]
        while x % 2 == 0:
            x //= 2
        if x == 1:
            count += 1
    if count == n:
        flag = True
        print('Найденный столбец: ')
        for j in range(n):
            print(f'{a[j][i]:^5.2f}')
        break
if n <= 0:
    print('Массив пуст')
elif not flag:
    print('Такого столбца нет')
