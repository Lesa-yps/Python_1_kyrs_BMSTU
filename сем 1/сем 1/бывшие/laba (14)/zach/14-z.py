# Талышева ИУ7-15Б
# (бинарное) название сериала_продолжительность(вещественное)
# 1) выбор файла (проверить)
# 2) вывести данные <= введенной продолжительности и записать их в файл

import struct as st

fmt = '512sf'
len_one_str = st.calcsize(fmt)

def chek(s):
    flag = 1
    if len(s) != 2:
        flag = 0
    else:
        if s[0] == '':
            flag = 0
        else:
            try:
                k = float(s[1])
            except Exception:
                flag = 0
    return flag

def choose_file():
    f = None
    while f == None :
        f = str(input('Введите название входного файла: '))
        try:
            f_in = open(f, 'rb')
        except Exception:
            print('Ошибка выбора файла. Повторите попытку.')
            f = None
        else:
            try:
                b1 = f_in.read(len_one_str)
                while b1 != b'':
                    b2 = st.unpack(fmt, b1)
                    flag = chek(b2)
                    if flag == 0:
                        print('Содержимое файла не соответствует программе.')
                        print('Повторите попытку ввода названия входного файла.')
                        f = None
                        break
                    b1 = f_in.read(len_one_str)
            except Exception:
                print('Ошибка выбора файла. Повторите попытку.')
                f = None
            else:
                print('Файл для работы выбран.')
            f_in.close()
    return f

def real_work(f):
    m = None
    while m == None:
        try:
            m = float(input('\nВведите максимальную, инересующую Вас, продолжительность сериала: '))
        except Exception:
            print('Ошибка: должно быть введено вещественное число. Повторите попытку.')
    f_in = open(f, 'rb')
    f_out = open('file.bin', 'wb')
    flag = 0
    b1 = f_in.read(len_one_str)
    while b1 != b'':
        b2 = st.unpack(fmt, b1)
        if float(b2[1]) <= m:
            f_out.write(b1)
            flag = 1
        b1 = f_in.read(len_one_str)
    f_in.close()
    f_out.close()
    if flag == 0:
        print('\nСтрок с искомымыи значениями в базе данных не найдено.')
    else:
        print('\nДанные записаны в файл "D:/temp/TAL/file.bin".')
    return flag

def write_file():
    print('\nИскомые данные из файла "D:/temp/TAL/file.bin":\n')
    with open('file.bin', 'rb') as f_in:
        b1 = f_in.read(len_one_str)
        while b1 != b'':
            b2 = st.unpack(fmt, b1)
            l = str(b2[0])[1:]
            for i in range(len(l) - 2):
                    if (l[i] + l[i + 1] + l[i + 2]) == 'x00':
                        break
            l = l[1:(i - 1)]                  
            print(l, '{:5.2}'.format(b2[1]))
            b1 = f_in.read(len_one_str)    

f = choose_file()
flag = real_work(f)
if flag == 1:
    write_file()
        
