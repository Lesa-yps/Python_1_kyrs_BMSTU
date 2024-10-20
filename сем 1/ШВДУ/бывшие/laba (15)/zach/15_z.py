# Талышева ИУ7-15Б
# сформировать бинарный файл из целых чисел и отзеркалить

import struct as st

fmt = '<i'
los = st.calcsize(fmt)

f = None
while f == None:
    f = str(input('Введите путь к файлу: '))
    try:
        file = open(f, 'wb')
    except Exception:
        print('Ошибка выбора файла. Повторите попытку.')
        f = None
print('Файл для работы выбран.')
file.close()

n = None
while n == None:
    try:
        n = int(input('Введите количество чисел, которое необходимо записать в файл: '))
    except Exception:
        print('Ошибка: должно быть введено целое число. Повторите попытку.')
    else:
        if n < 0:
            print('Ошибка: количество строк не может быть отрицательным. Повторите попытку.')
            n = None
        elif n == 0:
            print('Введено нулевое количество чисел. Файл очищен.')

with open(f, 'wb') as file:
    for i in range(n):
        x = None
        while x == None:
            try:
                x = int(input('Введите число №{}, которое необходимо записать в файл: '.format(i + 1)))
            except Exception:
                print('Ошибка: должно быть введено целое число. Повторите попытку.')
        x1 = st.pack(fmt, x)
        file.write(x1)

if n != 0:
    with open(f, 'r+b') as file:
        c = n - 2
        while c > -1:
            b1 = file.read(los)
            file.seek(c * los, 1)
            b2 = file.read(los)
            file.seek(-1 * los, 1)
            file.write(b1)
            file.seek(-1 * (c + 2) * los, 1)
            file.write(b2)
            c -= 2

with open(f, 'rb') as file:
    if n > 1:
        print('\nИзменённое содержимое файла: \n')
    elif n == 1:
        print('\nСодержимое файла: \n')
    for i in range(n):
        b1 = file.read(los)
        b2 = st.unpack(fmt, b1)[0]
        print(b2)
