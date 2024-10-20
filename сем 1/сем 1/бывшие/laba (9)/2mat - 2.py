# Талышева ИУ7-15Б
# Программа поворачивает квадратную целочисленную матрицу на 90 градусов по часовой стрелке, 
# затем на 90 градусов против часовой стрелки и выводит исходную, промежуточную и итоговую матрицы. 

# Ввод матрицы
n = int(input('Введите количество строк матрицы: '))
while n < 0:
  print('Неприемлемый ввод. Повторите попытку')
  n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
while n != m:
        print('Неверный ввод. Матрица должна быть квадратной. Повторите попытку.')
        n = int(input('Введите количество строк матрицы: '))
        m = int(input('Введите количество столбцов матрицы: '))
if n == 0 or m == 0:
    print('Матрица пуста')
else:
    a = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = int(input('Введите элемент в строке № {} столбце № {}: '.format(i + 1, j + 1)))
    # Вывод исходной матрицы
    print('Исходная матрица: ')
    for i in range(n):
        print('   ', end = '')
        for j in range(n):
            print(f'{a[i][j]:<7d}', end = (' ' * (8 - len(f'{a[i][j]:<7d}'))))
        print()
    # Проходимся по матрице и меняем местами по 4 элемента,
    # поворачивая матрицу на 90 градусов по часовой стрелке
    for i in range(round(n // 2)):
        for j in range(i, n - i - 1):
            a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i], a[i][j]\
                   = a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i]
    # Проверка на наличие элементов в матрице
    if n <= 0:
        print('Массив пуст')
    else:
        # Вывод промежуточной матрицы
        print('Промежуточная матрица: ')
        for i in range(n):
            print('   ', end = '')
            for j in range(n):
                print(f'{a[i][j]:<7d}', end = (' ' * (8 - len(f'{a[i][j]:<7d}'))))
            print()
        # Проходимся по матрице и меняем местами по 4 элемента,
        # поворачивая матрицу на 90 градусов против часовой стрелки
        for i in range(round(n // 2)):
                for j in range(i, n - i - 1):
                    a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i]\
                             = a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i], a[i][j]
        # Вывод итоговой матрицы
        print('Итоговая матрица: ')
        for i in range(n):
            print('   ', end = '')
            for j in range(n):
                print(f'{a[i][j]:<7d}', end = (' ' * (8 - len(f'{a[i][j]:<7d}'))))
            print()

