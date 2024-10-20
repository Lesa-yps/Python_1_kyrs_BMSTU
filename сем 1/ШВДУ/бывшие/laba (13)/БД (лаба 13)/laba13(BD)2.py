''' Талышева ИУ7-15Б
Программа позволяет с помощью меню выполнить следующие действия:
0. Выйти из программы
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в конец базы данных
5. Поиск по одному полю
6. Поиск по двум полям
'''

# Функция проверяет строку на соответствие программе
def test_str(s, w_r):
    l = s.split(',')
    flag = True
    # Проверяется количество полей
    if len(l) != 4:
            flag = False
            if w_r == 'w': print('Неверный ввод. Количество полей должно быть равно 4.')
    else:
            # Функция проверяет первое поле на соответствие программе
            for i in range(len(l[0])):
                    if not l[0].isalpha():
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. В первом поле должна быть фамилия студента.')
                        break
            if len(l[0]) == 0:
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. В первом поле должна быть фамилия студента.')
            # Функция проверяет второе поле на соответствие программе
            if len(l[0]) == 0:
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. Во втором поле должно быть число (балл  студента по программированию).')
            elif l[1][0] == '-' and l[1][1:].isdigit():
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. Во втором поле должно быть неотрицательное число (балл  студента по программированию).')
            elif not l[1].isdigit():
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. Во втором поле должно быть целое число (балл  студента по программированию).')
            elif not 0 <= int(l[1]) <= 100:
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. Во втором поле должно быть число от 0 до 100 (балл  студента по программированию).')
            # Функция проверяет третье поле на соответствие программе
            if l[2] != 'зачет' and l[2] != 'незачет':
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. В третьем поле должен быть "зачет" или "незачет" (через "е") по ангему.')
            # Функция проверяет четвертое поле на соответствие программе
            l[3] = l[3].rstrip('\n')
            if len(l[0]) == 0:
                        flag = False
                        if w_r == 'w': print('Ошибка ввода. Во четвёртом поле должно быть число (стипендия студента).')
            elif l[3][0] == '-':
                    flag = False
                    if w_r == 'w': print('Ошибка ввода. В четвёртом поле должно быть неотрицательное число (стипендия студента).')
            else:
                fl = True
                puf = False
                for i in l[3]:
                        if not i.isdigit() and i != '.':
                            fl = False
                            break
                        else:
                            puf = True
                if not puf:
                    flag = False
                    if w_r == 'w': print('Ошибка ввода. В четвёртом поле должно быть число (стипендия студента).')
                elif not fl or l[3].count('.') > 1:
                    flag = False
                    if w_r == 'w': print('Ошибка ввода. В четвёртом поле должно быть число (стипендия студента).')
                elif fl:
                    if 0 > float(l[3]):
                            flag = False
                            if w_r == 'w': print('Ошибка ввода. В четвёртом поле должно быть неотрицательное число (стипендия студента).')
    return flag


# Функция выбирает файл для работы
def choose_file(n):
    try:
        f = str(input('Введите путь к файлу: '))
        if n == 2: file = open(f, 'w')
        else: file = open(f)
        file.close()
    # Проверка файла
    except FileNotFoundError:
        if n == 2: print('Введено некорректное имя файла.')
        else: print('Файл не найден.')
        f = None
    except PermissionError:
        print('Права доступа к файлу ограничены.')
    except Exception:
        print('Ошибка выбора файла.')
        f = None
    else:
        try:
            file = open(f, encoding = 'utf-8')
            flag = True
            for s in file:
                flag = test_str(s, 'r')
                if not flag:
                    print('Выбранный файл не соответствует программе')
                    f = None
                    break
            file.close()
        except Exception:
            print('Ошибка выбора файла.')
            f = None
        else:
            if flag:
                try:
                    file = open(f, 'a')
                except PermissionError:
                    print('Внимание: права доступа к файлу ограничены! Некоторые пункты меню могут быть недоступны.')
                    print('Файл для работы выбран.')
                except Exception:
                    print('Ошибка выбора файла.')
                    f = None
                else:
                    print('Файл для работы выбран.')
                    file.close()                
    return f

# Функция записывает в файл новые данные
def w_file(f, reg):
    if f == None and reg == 'a':
        print('Файл для работы не выбран')
    # Открывется файл
    else:
        if f == None and reg == 'w':
            f = choose_file(2)
        if f != None:
            try:
                file = open(f, reg, encoding = 'utf-8')
            except PermissionError:
                print('Внимание: права доступа к файлу ограничены! Запись в файл недоступна.')
            except Exception:
                print('Ошибка выбора файла.')
            else:
                # Вводится количество строк
                m = None
                while m == None:
                    try:
                        m = int(input('Введите количество строк: '))
                    except ValueError:
                        print('Ошибка ввода. Введённое значение должно быть целым числом. Повторите попытку.')
                    else:
                        if m <= 0:
                            if reg == 'a':
                                print('Введённое количество строк неположительное. Файл не изменён.')
                            else:
                                print('Введённое количество строк неположительное. Файл пуст.')
                if m > 0:
                    for i in range(m):
                        # Ввод новой строки и её проверка
                        s = None
                        while s == None:
                            s = str(input('Введите строку базы данных с полями разделёнными запятыми: '))
                            flag = test_str(s, 'w')
                            if not flag:
                                print('Повторите попытку ввода.')
                                s = None
                        # Запись строки в файл
                        file.write(s + '\n')
                    print('Данные записаны.')
                file.close()
    return f

# Функция выводит содержимое базы данных
def print_file(f, ):
    if f == None:
        print('Файл для работы не выбран')
    # Открывется файл
    else:
        with open(f, 'r', encoding = 'utf-8') as file:
            flag = False
            for i in file:
                flag = True
            if not flag:
                print('\nБаза данных пуста')
                print('\n')
        if flag:
            with open(f, 'r', encoding = 'utf-8') as file:
                print('\nСодержимое базы данных: \n')
                s0 = s3 = ''
                for i in file:
                    if len(i[0]) > len('фамилия студента') and len(s0) < (len(i[0]) - len('фамилия студента')):
                        s0 = ' ' * (len(i[0]) - len('фамилия студента'))
                    if len(i[3]) > len('размер стипендии') and len(s3) < (len(i[3]) - len('фамилия_студента')):
                        s3 = ' ' * (len(i[3]) - len('размер стипендии'))
            with open(f, 'r', encoding = 'utf-8') as file:
                k0 = len('фамилия студента' + s0)
                k1 = len('баллы по программированию')
                k2 = len('зачет/незачет по ангему')
                k3 = len('размер стипендии' + s3)
                print('-' * (k0 + k1 + k2 + k3 + 9))
                print('|', ' ' * (len(s0) // 2), 'фамилия студента' , ' ' * (len(s0) - (len(s0) // 2)),\
                      '|', ' баллы по программированию ', '|', ' зачет/незачет по ангему ',\
                      '|', ' ' * (len(s3) // 2), 'размер стипендии', ' ' * (len(s3) - (len(s3) // 2)),'|', sep = '')
                print('-' * (k0 + k1 + k2 + k3 + 9))
                for t in file:
                    l = t.split(',')
                    print('|', ' ' * ((k0 - len(l[0])) // 2), l[0], ' ' * (k0 - len(l[0]) - ((k0 - len(l[0])) // 2)),'| ',\
                          ' ' * ((k1 - len(l[1])) // 2), l[1], ' ' * (k1 + 1 - len(l[1]) - ((k1 - len(l[1])) // 2)),'| ',\
                          ' ' * ((k2 - len(l[2])) // 2), l[2], ' ' * (k2 + 1 - len(l[2]) - ((k2 - len(l[2])) // 2)),'|',\
                          ' ' * ((k3 - len(l[3])) // 2), l[3].rstrip('\n'), ' ' * (k3 + 1 - len(l[3]) - ((k3 - len(l[3])) // 2)),'|', sep ='')
                print('-' * (k0 + k1 + k2 + k3 + 9))             
    return f

def strk_v2():
        strk = None
        # Ввод пользователем искомого значения
        while strk == None:
            strk = str(input('\nВыберите значение, которое должно находится в поле №3 в искомых строках, ("зачет" или "незачет"): '))
            if strk != 'зачет' and strk != 'незачет':
                print('Ошибка ввода. Должно быть введено "зачет" или "незачет" (через "е"). Повторите попытку.')
                strk = None
        return strk

def strk_v3():
    strk2 = None
    while strk2 == None:
        try:
                strk2 = float(input('\nВыберите значение, которое должно находится в поле №4 в искомых строках, (размер стипендии): '))
        except ValueError:
                print('Ошибка ввода. Должно быть введено число (размер стипендии). Повторите попытку.')
        else:
                if strk2 < 0:
                        print('Ошибка ввода. Должно быть введено неотрицательное число (размер стипендии). Повторите попытку.')
                        strk2 = None
    return strk2

# Функция выполняет поиск строк по 1 или 2 полям (№3 и №4)
def find_1_2(f, n):
    if f == None:
        print('Файл для работы не выбран')
    # Открывется файл
    else:
            strk = strk_v2()
            if n == 6:
                strk2 = strk_v3()
            # Поиск значения по строкам
            flag = True
            with open(f, 'r', encoding = 'utf-8') as file:
                for i in file:
                    l = i.split(',')
                    puf = False
                    if l[2] == strk:
                        if n == 6:
                            if (strk2 - 10**(-10)) <= float(l[3]) <= (strk2 + 10**(-10)):
                                puf = True
                        else:
                            puf = True
                        if flag and puf:
                            print('Искомые строки: \n')
                            flag = False
                            break
            if not flag:
                with open(f, 'r', encoding = 'utf-8') as file:
                    for line in file:
                        i = line.split(',')
                        s0 = s3 = ''
                        if len(i[0]) > len('фамилия студента') and len(s0) < (len(i[0]) - len('фамилия студента')):
                            s0 = ' ' * (len(i[0]) - len('фамилия студента'))
                        if len(i[3]) > len('размер стипендии') and len(s3) < (len(i[3]) - len('фамилия_студента')):
                            s3 = ' ' * (len(i[3]) - len('размер стипендии'))
                with open(f, 'r', encoding = 'utf-8') as file:
                    k0 = len('фамилия студента' + s0)
                    k1 = len('баллы по программированию')
                    k2 = len('зачет/незачет по ангему')
                    k3 = len('размер стипендии' + s3)
                    print('-' * (k0 + k1 + k2 + k3 + 9))
                    print('|', ' ' * (len(s0) // 2), 'фамилия студента' , ' ' * (len(s0) - (len(s0) // 2)), '|', ' баллы по программированию ',\
                          '|', ' зачет/незачет по ангему ','|', ' ' * (len(s3) // 2), 'размер стипендии',\
                          ' ' * (len(s3) - (len(s3) // 2)),'|', sep = '')
                    print('-' * (k0 + k1 + k2 + k3 + 9))
                    for m in file:
                        l = m.split(',')
                        puf = False
                        if l[2] == strk:
                            if n == 6:
                                if (strk2 - 10**(-10)) <= float(l[3]) <= (strk2 + 10**(-10)):
                                    puf = True
                            else:
                                puf = True
                        if puf:
                            print('|', ' ' * ((k0 - len(l[0])) // 2), l[0], ' ' * (k0 - len(l[0]) - ((k0 - len(l[0])) // 2)),'| ',\
                              ' ' * ((k1 - len(l[1])) // 2), l[1], ' ' * (k1 + 1 - len(l[1]) - ((k1 - len(l[1])) // 2)),'| ',\
                              ' ' * ((k2 - len(l[2])) // 2), l[2], ' ' * (k2 + 1 - len(l[2]) - ((k2 - len(l[2])) // 2)),'|',\
                              ' ' * ((k3 - len(l[3])) // 2), l[3].rstrip('\n'), ' ' * (k3 + 1 - len(l[3]) - ((k3 - len(l[3])) // 2)),'|', sep ='')
                    print('-' * (k0 + k1 + k2 + k3 + 9))   
            if flag:
                print('Подходящей строки нет в базе данных.')
            print('\n')
    return f

# Цикл прекратит работу при вводе 0
n = None
f = None
while n != 0:
    # Вывод на экран пояснений
    print('\nПрограмма работает с базами данных, имеющими структуру:\n\
            фамилия_студента,баллы_по_программированию,зачет/незачет_по_ангему,размер_стипендии')
    print('*Поля разделены запятыми')
    # Вывод на экран меню
    print('\nМЕНЮ:')
    print('          0. Выйти из программы.\n\
          1. Выбрать файл для работы.\n\
          2. Инициализировать базу данных.\n\
          3. Вывести содержимое базы данных.\n\
          4. Добавить запись в конец базы данных.\n\
          5. Поиск по одному полю (поле №3 зачет/незачет_по_ангему).\n\
          6. Поиск по двум полям (поле №3 зачет/незачет_по_ангему и поле №4 размер_стипендии).')
    # Ввод пользователем номера действия
    n = None
    while n == None:
        try:
            n = int(input('\nВыберите действие которое необходимо совершить: '))
        except ValueError:
            print('Ошибка ввода. Введённое значение должно быть целым числом. Повторите попытку.')
        else:
            if n < 0 or n > 6:
                print('Ошибка ввода. Введённое значение должно быть цифрой, лежащей в отрезке от 0 до 6. Повторите попытку.')
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
       f = choose_file(1) 
    # При вводе действия 2 инициализируется база данных
    elif n == 2:
        f = w_file(f, 'w')
    # При вводе действия 3 выводится содержимое базы данных     
    elif n == 3:
        f = print_file(f) 
    # При вводе действия 4 добавляется запись в конец базы данных
    elif n == 4:
        f = w_file(f, 'a')
    # При вводе действия 5 происходит поиск по одному полю
    elif n == 5:
        f = find_1_2(f, n)
    # При вводе действия 6 происходит поиск по двум полям
    elif n == 6:
        f = find_1_2(f, n)
    # При вводе действия 0 программа заканчивает работу
    elif n == 0:
        print('\nСеанс окончен.\n')
