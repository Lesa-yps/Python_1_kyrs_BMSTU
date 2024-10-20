''' Талышева ИУ7-15Б
Программа позволяет с помощью меню выполнить следующие действия:
0. Выйти из программы
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных (пользователь указывает номер позиции, в которую должна быть вставлена запись)
5. Удалить произвольную запись из базы данных (пользователь указывает номер удаляемой записи)
6. Поиск по одному полю
7. Поиск по двум полям
'''
import struct as st
import os.path

main = '| фамилия студента | баллы по программированию | зачет/незачет по ангему | размер стипендии |'
ch = len(main)
eps = 10**(-10)

def hat():
    print('-' * (ch))
    print(main)
    print('-' * (ch))

# Функция преобразует строку базы данных в удобный для обработки и восприятия пользователем список
def true_unpack(s):
    l = [0,0,0,0]
    if str(s[0]).find('0') != -1:
        l[0] = str(s[0])[2:(str(s[0]).find('0') - 2)]
    else:
        l[0] = str(s[0])[2:-1]
    l[1] = int(s[1])
    if str(s[2]).find('0') != -1:
        l[2] = str(s[2])[2:(str(s[2]).find('0') - 2)]
    else:
        l[2] = str(s[2])[2:-1]
    l[3] = float(s[3])
    if len(str(l[3])[(str(l[3]).find('.') + 1):]) > 2:
        l[3] = float(str(l[3])[:(str(l[3]).find('.') + 3)])
    return l

# Функция проверяет подходит ли строка файла программе
def test_str_bin(s):
    flag = True
    if len(s) != 4:
        flag = False
    else:
        try:
           l = true_unpack(s)
           if len(l[0]) > 15:
               flag = False
           if not 0 <= l[1] <= 100:
               flag = False
           if l[2] != 'offset' and l[2] != 'fail':
               flag = False
           if len(str(l[3])[:str(l[3]).find('.')]) > 5:
                flag = False
        except Exception:
            flag = False
    return flag

# В этой функции позователь выбирает файл для работы и происходит проверка этого файла
def choose_file():
    # Ввод пути к файлу
    f = str(input('Введите путь к файлу: '))
    if f == '':
        print('Введена пустая строка.')
    else:
        # Поверка файла
        try:
            file = open(f, 'rb')
        except FileNotFoundError:
            print('Файл не найден')
            f = None
        except PermissionError:
            print('Ошибка доступа к файлу.')
            f = None
        except Exception:
            print('Ошибка выбора файла')
            f = None
        else:
            # Проверка содержимого файла на соответствие программе
            flag = True
            try:
                while i := file.read(st.calcsize('<15si6sf')):
                    s = st.unpack('<15si6sf', i)
                    flag = test_str_bin(s)
                    if not flag:
                        print('Файл не соответствует прорамме.')
                        f = None
                        break
                file.close()
            except Exception:
                print('Файл не соответствует прорамме.')
                f = None
            else:
                if f != None:
                    try:
                        file = open(f, 'ab')
                    except Exception:
                        print('Запись в файл ограничена. Некоторые пункты меню могут быть недоступны.')
                    else:
                        file.close()
                if flag:
                    print('Файл для работы выбран.')
    return f

# Функция принимает значения полей от пользователя и состевляет строку базы данных
def read_chek_str():
    l = [None] * 4
    # Ввод и проверка первого поля
    while l[0] == None:
                      l[0] = str(input('Введите фамилию студента (на английском языке, максимальная длина = 15): '))
                      if len(l[0]) == 0:
                        print('Ошибка: введена пустая строка.')
                        l[0] = None
                      elif len(l[0]) > 15:
                        l[0] = l[0][:15]
                        print('Длина строки была больше 15, она была обрезана.')
                      else:
                        for i in l[0]:
                           if not i.isalpha():
                                 print('Ошибка: фамилия должна состоять из букв.')
                                 l[0] = None
                                 break
                           if i not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                                 print('Ошибка: фамилия должна состоять из букв латинского алфавита.')
                                 l[0] = None
                                 break
                      if l[0] == None:
                         print('Повторите попытку:')
    # Ввод и проверка второго поля
    while l[1] == None:
                        try:
                            l[1] = int(input('Введите балл студента по программированию [0;100]: '))
                        except ValueError:
                            print('Ошибка: введенное значение должно быть целым числом')
                        except Exception:
                            print('Ошибка ввода.')
                        else:
                            if not 0 <= l[1] <= 100:
                                print('Ошибка: балл должен находиться в промежутке [0;100].')
                                l[1] = None
                        if l[1] == None:
                            print('Повторите попытку:')
    # Ввод и проверка третьего поля
    while l[2] == None:
                        l[2] = str(input('Введите зачёт - "offset" или незачет - "fail" у студента по ангему: '))
                        if l[2] == '':
                            print('Ошибка: введена пустая строка.')
                            l[2] = None
                        elif l[2] != 'offset' and l[2] != 'fail':
                            print('Ошибка: должен быть введён зачёт - "offset" или незачет - "fail" у студента по ангему.')
                            l[2] = None
                        if l[2] == None:
                            print('Повторите попытку:')
    # Ввод и проверка четвертого поля
    while l[3] == None:
                        try:
                            l[3] = float(input('Введите стипендию студента (максимальная длина до точки 5 символов, после точки 2 символа): '))
                        except ValueError:
                            print('Ошибка: введенное значение должно быть числом.')
                        except Exception:
                            print('Ошибка ввода.')
                        else:
                            if 0 > l[3]:
                                print('Ошибка: стипендия должна быть неотрицательной.')
                                l[3] = None
                            if len(str(l[3])[:str(l[3]).find('.')]) > 5 or len(str(l[3])[(str(l[3]).find('.') + 1):]) > 2:
                                    print('Ошибка: максимальная длина числа до точки 5 символов, после точки 2 символа.')
                                    l[3] = None
                        if l[3] == None:
                            print('Повторите попытку:')
    # Строки преобразуются в байтовые строки
    l[0] = bytes(l[0], encoding = 'utf-8')
    l[2] = bytes(l[2], encoding = 'utf-8')
    return l

# Функция инициализирует базу данных и записывает в неё введённые строки    
def w_file():
    f = str(input('Введите путь к файлу: '))
    if f == '':
        print('Введена пустая строка.')
    else:
        try:
            file = open(f, 'wb')
        except PermissionError:
            print('Ошибка доступа к файлу.')
            f = None
        except Exception:
            print('Ошибка выбора файла')
            f = None
        else:
            n = None
            puf = False
            # Ввод количества строк
            while n == None:
                try:
                    n = int(input('Введите количество строк: '))
                except ValueError:
                    print('Ошибка: должно быть введено целое число')
                except Exception:
                    print('Ошибка ввода')
                else:
                    if n <= 0:
                        print('Введено неположительное число строк. Файл был очищен.')
                        puf = True
                if n == None:
                    print('Повторите попытку: ')
            if not puf:
                # Запись строк в файл
                for w in range(n):
                    l = read_chek_str()
                    m = st.pack('<15si6sf', l[0], l[1], l[2], l[3])
                    file.write(m)
                    print('Cтрока записана.')
                file.close()
    return f

# Функция выводит базу данных из файла на экран
def print_file(f):
    puf = False
    if f == None:
        print('Файл для работы не выбран.')
    else:
        # Вывод базы данных в виде таблицы из файла на экран
        with open(f, 'rb') as file:
            while i := file.read(st.calcsize('<15si6sf')):
                    if not puf:
                        hat()
                        puf = True
                    s = st.unpack('<15si6sf', i)
                    l = true_unpack(s)
                    print('|', '{:^18}'.format(l[0]), '|', '{:^27d}'.format(l[1]), '|', '{:^25}'.format(l[2]),\
                          '|', '{:^18.2f}'.format(l[3]), '|', sep = '')
            if puf: print('-' * (ch))
        if not puf:
            print('База данных пуста.')

# Функция добавляет строку в произвольное место базы данных
def app_in_file(f):
    # Проверка и открытие файла
    if f == None:
        print('Файл для работы не выбран.')
    else:
        try:
            file = open(f, 'r+b')
        except PermissionError:
            print('Права доступа к файлу ограничены. Этот пункт меню недоступен.')
        except Exception:
            print('Ошибка открытия файла. Перевыберете файл, пожалуйста.')
        else:
            # Ввод номера добавляемой строки
            j = None
            while j == None:
                try:
                    j = int(input('Введите номер добавляемой строки\n\
(если количество строк в файле будет меньше \n\
введённого значения, строка запишется в конец базы данных): '))
                except ValueError:
                    print('Ошибка: должно быть введено целое число. Повторите попытку.')
                except Exception:
                    print('Ошибка ввода. Повторите попытку.')
                else:
                    j -= 1
                    if j < 0:
                        j = 0
                        print('Был введён неположительный номер строки. Строка будет записана в начало базы данных.')
            flag = False
            file2 = open(f, 'rb')
            c2 = file2.read(st.calcsize('<15si6sf'))
            i = 0
            while j >= i:
                   if i == j:
                       i += 1
                       flag = True
                       # Запись строки на нужное место базы данных
                       l = read_chek_str()
                       m = st.pack('<15si6sf', l[0], l[1], l[2], l[3])
                       file.write(m)
                       # Сдвиг остальных строк базы данных
                       while c1 := file2.read(st.calcsize('<15si6sf')):
                           c2_more = c1
                           file.write(c2)
                           c2 = c2_more
                       file.write(c2)
                   else:
                        i += 1
                        c2 = file2.read(st.calcsize('<15si6sf'))
                        b2 = file.read(st.calcsize('<15si6sf'))
                        if b2 == c2 == b'':
                            break
            # Если номер строки больше количества строк в файле, строка запишется в конец базы данных
            if not flag:
                    l = read_chek_str()
                    m = st.pack('<15si6sf', l[0], l[1], l[2], l[3])
                    file.write(m)
            print('Cтрока записана.')
            file2.close()
            file.close()               

# Удаление строки базы данных
def del_in_file(f):
    # Проверка и открытие файла
    if f == None:
        print('Файл для работы не выбран.')
    else:
        try:
            file = open(f, 'r+b')
        except PermissionError:
            print('Права доступа к файлу ограничены. Этот пункт меню недоступен.')
        except Exception:
            print('Ошибка открытия файла. Перевыберете файл, пожалуйста.')
        else:
            puf = False
            # Ввод номера удаляемой строки
            j = None
            while j == None:
                try:
                    j = int(input('Введите номер удаляемой строки: '))
                except ValueError:
                    print('Ошибка: должно быть введено целое число. Повторите попытку.')
                except Exception:
                    print('Ошибка ввода. Повторите попытку.')
                else:
                    j -= 1
                    if j < 0:
                        print('Был введён неположительный номер строки. База данных не изменена.')
                        puf = True
            flag = False
            file2 = open(f, 'rb')
            c2 = file2.read(st.calcsize('<15si6sf'))
            i = 0
            while j >= i:
                   if i == j:
                       flag = True
                       i += 1
                       # Строки базы данных после удаляемой сдвигаются
                       while c1 := file2.read(st.calcsize('<15si6sf')):
                           c2 = c1
                           file.write(c2)
                       # Последняя строка, которая стала повторяющейся, обрезается
                       b2 = file.read(st.calcsize('<15si6sf'))
                       file.truncate(os.path.getsize(f) - len(b2))
                   else:
                        i += 1
                        c2 = file2.read(st.calcsize('<15si6sf'))
                        b2 = file.read(st.calcsize('<15si6sf'))
                        if b2 == c2 == b'':
                            break
            if flag:
                print('Cтрока удалена.')
            elif not puf:
                print('Номер удаляемой строки больше длины файла. База данных не изменена.')
            file2.close()
            file.close()

# Функция осуществляет поиск по одному/двум полям
def find_1_2(f, n):
    if f == None:
        print('Файл для работы не выбран.')
    else:
        # Вводи проверка искомого значения в поле №3
        str2 = str3 = None
        while str2 == None:
                        str2 = str(input('Введите искомое значение поля №3: зачёт - "offset" или незачет - "fail" у студента по ангему: '))
                        if str2 == '':
                            print('Ошибка: введена пустая строка.')
                            str2 = None
                        elif str2 != 'offset' and str2 != 'fail':
                            print('Ошибка: должен быть введён зачёт - "offset" или незачет - "fail" у студента по ангему.')
                            str2 = None
                        if str2 == None:
                            print('Повторите попытку:')
        if n == 7:
            # Если осуществляется поиск по двум полям вводится и проверяется искомое значение в поле №4
            while str3 == None:
                        try:
                            str3 = float(input('Введите искомое значение поля №4: стипендию студента: '))
                        except ValueError:
                            print('Ошибка: введенное значение должно быть числом.')
                        except Exception:
                            print('Ошибка ввода.')
                        else:
                            if 0 > str3:
                                print('Ошибка: стипендия должна быть неотрицательной.')
                                str3 = None
                        if str3 == None:
                            print('Повторите попытку:')
        # Проходимся по файлу и выводим подходящие строки в таблице
        flag = False
        with open(f, 'rb') as file:
            while i := file.read(st.calcsize('<15si6sf')):
                    s = st.unpack('<15si6sf', i)
                    l = true_unpack(s)
                    if l[2] == str2 and (n == 6 or str3 - 10**(-10) <= l[3] <= str3 + 10**(-10)):
                        if not flag:
                            hat()
                        print('|', '{:^18}'.format(l[0]), '|', '{:^27d}'.format(l[1]), '|', '{:^25}'.format(l[2]),\
                              '|', '{:^18.2f}'.format(l[3]), '|', sep = '')
                        flag = True
        if flag:
            print('-' * (18 + 27 + 25 + k3 + 6))
        else:
            if n == 6:
                print('Строк с искомым значением в базе данных нет.')
            else:
                print('Строк с искомыми значениями в базе данных нет.')

# Цикл прекратит работу при вводе 0
n = None
f = None
while n != 0:
    # Вывод на экран пояснений
    print('\nПрограмма работает с базами данных, хранящимися в бинарном виде, имеющими структуру:\n\n\
            фамилия_студента|баллы_по_программированию|зачет/незачет_по_ангему|размер_стипендии')
    # Вывод на экран меню
    print('\nМЕНЮ:')
    print('          0. Выйти из программы.\n\
          1. Выбрать файл для работы.\n\
          2. Инициализировать базу данных.\n\
          3. Вывести содержимое базы данных.\n\
          4. Добавить запись в произвольное место базы данных.\n\
          5. Удалить произвольную запись из базы данных.\n\
          6. Поиск по одному полю (поле №3 зачет/незачет_по_ангему).\n\
          7. Поиск по двум полям (поле №3 зачет/незачет_по_ангему и поле №4 размер_стипендии).')
    # Ввод пользователем номера действия
    n = None
    while n == None:
        try:
            n = int(input('\nВыберите действие которое необходимо совершить: '))
        except ValueError:
            print('Ошибка ввода. Введённое значение должно быть целым числом. Повторите попытку.')
        else:
            if n < 0 or n > 7:
                print('Ошибка ввода. Введённое значение должно быть цифрой, лежащей в отрезке от 0 до 7 включительно. Повторите попытку.')
                n = None
            elif n == 0:
                a = None
                while a != 'y' and a != 'n':
                    if a == None:
                        a = str(input('Вы уверены, что хотите завершить сеанс? Нажмите "y" - "да" или "n" - "нет": '))
                    else:
                        a = str(input('Ошибка ввода. Введите "y" - "да" или "n" - "нет": '))
                if a == 'n':
                    n = None
    # При вводе действия 1 выбирается файл для работы 
    if n == 1:
       f = choose_file() 
    # При вводе действия 2 инициализируется база данных
    elif n == 2:
        f = w_file()
    # При вводе действия 3 выводится содержимое базы данных     
    elif n == 3:
        print_file(f) 
    # При вводе действия 4 добавляется запись в произвольное место базы данных
    elif n == 4:
        app_in_file(f)
    # При вводе действия 5 удаляется произвольная база данных
    elif n == 5:
        del_in_file(f)
    # При вводе действия 5 происходит поиск по одному полю
    elif n == 6:
        find_1_2(f, n)
    # При вводе действия 6 происходит поиск по двум полям
    elif n == 7:
        find_1_2(f, n)
    # При вводе действия 0 программа заканчивает работу
    elif n == 0:
        print('\nСеанс окончен.\n')
