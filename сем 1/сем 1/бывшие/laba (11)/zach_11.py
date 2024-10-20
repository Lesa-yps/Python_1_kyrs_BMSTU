# Талышева ИУ7-15Б
# отсортировать массив Шейкером

n = None
while n == None:
    try:
        n = int(input('Введите количество элементов  массива: '))
    except ValueError:
        print('Ошибка ввода. Количество элементов должно быть целым числом. Повторите попытку.')
    else:
        if n <= 0:
            print('Ошибка ввода. Количество элементов должно быть положительным числом. Повторите попытку.')
            n = None
a = [0] * n
for i in range(n):
    a[i] = None
    while a[i] == None:
        try:
            a[i] = int(input('Введите элемент  массива №{}: '.format(i + 1)))
        except ValueError:
            print('Ошибка ввода. Элемент должен быть целым числом. Повторите попытку.')

# Шейкер
def Srt(x):
    k = 0
    for i in range(len(x)):
        flag = False
        for j in range(k, len(x) - k - 1):
            if x[j] > x[j + 1]:
                x[j + 1], x[j] = x[j], x[j + 1]
                flag = True
        for j in range(len(x) - k - 2, k - 1, -1):
            if x[j] > x[j + 1]:
                x[j + 1], x[j] = x[j], x[j + 1]
                flag = True
        if not flag:
            break
        k += 1
    return x

print('Отсортированный массив: ', *Srt(a))
