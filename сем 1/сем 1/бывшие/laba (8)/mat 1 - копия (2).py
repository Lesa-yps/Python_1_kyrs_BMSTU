# Талышева ИУ7-15Б
# Программа находит строку в введенной матрице с наименьшим количеством чётных элементов

# Ввод матрицы
n = int(input('Введите количество строк матрицы: '))
a = []
for i in range(n):
    a.append(list(map(float, input('Введите элементы строки матрицы через пробел: ').split())))
# Задаём переменную для сохранения индекса строки и минимального количества чётных элементов в строке
ind = None
cm = len(a[0]) + 1
# Проходимся по матрице
for i in range(n):
    # задаём счётчик количества чётных элементов в строке
    count = 0
    for j in range(len(a[i])):
        # если элемент чётный, увеличиваем счётчик
        if a[i][j] % 2 == 0:
            count += 1
    # Сравниваем значение счётчика с минимальным и сохранаяем индекс минимального
    if count < cm:
        cm = count
        ind = i
# Проверка на наличие элементов в массиве
if n <= 0:
    print('Массив пуст')
# Выводим искомую строку
else:
    for j in range(len(a[ind])):
        print(f'{a[ind][j]:^5.2f}', end = (' ' * (12 - len(f'{a[ind][j]:^5.2f}'))))
