''' Талышева ИУ7-15Б
Программа работает с бинарными файлами из целых 32-битных чисел,
реализовывает ввод чисел в файл (если файл существует - перезаписывает),
сортирует методом вставок с барьером
и выводит изменённое содержимое файла.'''

import struct as st

# Константы
fmt = '<i'
los = st.calcsize(fmt)

# В этой функции позователь выбирает файл для работы и происходит проверка этого файла
# (если файла нет, то он создаётся)
def choose_file():
    f = None
    while f == None:
        # Ввод пути к файлу
        f = str(input('Введите путь к файлу: '))
        if f == '':
            print('Введена пустая строка. Повторите попытку.')
            f = None
        else:
            # Поверка файла
            try:
                file = open(f, 'rb')
            except FileNotFoundError:
                file = open(f, 'wb')
                file.close()
                print('Файл был создан.')
            except PermissionError:
                print('Ошибка доступа к файлу.')
                f = None
            except Exception:
                print('Ошибка выбора файла')
                f = None
            else:
                try:
                    file = open(f, 'wb')
                except Exception:
                    print('Запись в файл ограничена. Повторите попытку.')
                    f = None
                else:
                    file.close()
                    print('Файл для работы выбран.')
    return f

# Вызов функции и получении пути к файлу
f = choose_file()

# Ввод количества строк
n = None
while n == None:
    try:
        n = int(input('Введите количество чисел, которые необходимо ввести: '))
    except Exception:
        print('Должно быть введено целое число. Повторите попытку.')
    else:
        if n < 0:
            print('Kоличество чисел должно быть неотрицательным. Повторите попытку.')
            n = None
        elif n == 0:
            print('Введено нулевое количество чисел. Файл очищен.')

# Запись чисел в файл
with open(f, 'wb') as file:
    for i in range(n):
        ch = None
        while ch == None:
            try:
                ch = int(input('Введите число №{}, которое необходимо записать в файл: '.format(i + 1)))
            except Exception:
                print('Должно быть введено целое число. Повторите попытку.')
        ch = st.pack(fmt, ch)
        file.write(ch)

# Cортировка чисел в файле методом вставок с барьером
with open(f, 'r+b') as file:
    wall = 2
    while wall <= n:
        file.seek(los * (wall - 1), 0)
        # Добавление "барьера"
        s_old = file.read(los)
        file.seek(0,0)
        while s := file.read(los):
            file.seek(-1 * los, 1)
            file.write(s_old)
            s_old = s
        file.write(s_old)
        file.seek(los * wall, 0)
        # Сами вставки
        now1 = file.read(los)
        now2 = st.unpack(fmt, now1)[0]
        wall += 1
        file.seek(-2 * los, 1)
        s1 = file.read(los)
        s2 = st.unpack(fmt, s1)[0]
        while int(s2) > int(now2):
            file.seek(-1 * los, 1)
            file.write(now1)
            file.write(s1)
            file.seek(-3 * los, 1)
            s1 = file.read(los)
            s2 = st.unpack(fmt, s1)[0]
        # Удаление "барьера"
        file.seek(los, 0)
        while b1 := file.read(los):
            file.seek(-2 * los, 1)
            file.write(b1)
            file.seek(los, 1)
        file.truncate(n*los)

# Вывод изменённого содержимого
if n != 0:
    flag = 0
    with open(f, 'rb') as file1:
        while s1 := file1.read(los):
            s = st.unpack(fmt, s1)
            if flag == 0:
                print('\nИзменённое содержимое файла:\n')
            print(s[0])
            flag = 1
    if flag == 0:
        print('Файл пуст.')
