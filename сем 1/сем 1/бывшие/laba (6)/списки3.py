''' Талышева ИУ7 - 15Б
Программа выводит К-тый экстремум в введенном массиве'''
# Ввод массива
n = int(input('Введите количество элементов массива: '))
while n < 0:
    n = int(input('Недопустимое количество элементов. Введите количество элементов массива: '))
a = [0] * n
for i in range(n):
    a[i] = float(input('Введите элемент массива: '))
# Ввод номера экстремума, который нужно вывести
K = int(input('Введите номер экстремума, который нужно вывести: '))
# Задаётся переменная для подсчёта количества экстремумов
count = 0
# Задаётся переменная - "метка" нахождения К-ого экстремума
flag = False
# Проходимся по списку со второго элемента и до предпоследнего
for i in range(1, n-1):
    # Если a[i] - экстремум, увеличиваем счётчик экстремумов на 1
    if (a[i-1] < a[i] and a[i+1] < a[i]) or (a[i-1] > a[i] and a[i+1] > a[i]):
        count += 1
        # Если текущий элемент равен K, выводим его и прерываем цикл
        if count == K:
            print (a[i])
            # Отмечаем в переменной, что К-тый экстремум был найден
            flag = True
            break
# Если К-тый экстремум не был найден, то выводим об этом сообщениеФ
if not flag:
    print ('Экстремум под искомым номером не найден')
