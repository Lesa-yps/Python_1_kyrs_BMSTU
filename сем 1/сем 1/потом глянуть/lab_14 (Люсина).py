#Фролова Людмила ИУ7-13Б
'''Программа позволяет работать с файлами, содержащими базы данных.'''


import struct as st
import os
'''f = open('d.bin','r')
s=st.unpack('=10sii',f.readline())
print(s)'''


#Выбор имени файла
def Choose(n,form):
    if os.path.exists(n):
        while True:
            try:
            #Проверка на то, подходит ли для работы программы выбранный файл
                with open(n,'rb') as file:
                    while i := file.read(st.calcsize(form)):
                        s = st.unpack(form, i)
                        print(s)

            except:
                print(1)
                return 'Файл не подходит для выбора.'
            else:
                break
        with open(n,'rb') as file:
            while i := file.read(st.calcsize(form)):
                line = st.unpack(form,i)
                if len(line) == 3:
                    while True:
                        try:
                            s1 = line[0].decode()
                            s2 = line[1]
                            s3 = line[2]
                            if not str(s2).isdigit() or not str(s3).isdigit():
                                return 'Файл не подходит для выбора.'
                            
                        except:
                            return 'Файл не подходит для выбора.'
                        else:
                            break
                else:
                    return 'Файл не подходит для выбора.'
        return n
    else:
        return None


#Инициализация базы данных   
def Base(name, m, column, form):
    i = 0
    with open (name, 'wb') as file:
        for i in range(m):
            while True:
                try:
                    st1 = input('Введите поле <Имя> {}-ой записи: '.format(i + 1))
                    if not st1.isalpha() or len(st1)>10:
                        raise Exception('В поле <Имя> должно быть введено одно слово,длиной не больше 10 символов!')
                except Exception as e:
                    print(e)
                else:
                    break
            while True:
                try:
                    st2 = input('Введите поле <Возраст {}-ой записи: '.format(i + 1))
                    if not st2.isdigit() or len(st2) > 10:
                        raise Exception('В поле <Возраст> должно быть введено одно целое положительное число, не превышающее 10^10!')    #Проверка на корректность введенных значений
                except Exception as e:
                    print(e)
                else:
                    break
            while True:
                try:
                    st3 = input('Введите поле <Вес> {}-ой записи: '.format(i + 1))
                    if not st3.isdigit() or len(st3) > 10:
                        raise Exception('В поле <Вес> должно быть введено одно целое положительное число, не превышающее 10^10!')    #Проверка на корректность введенных значений
                except Exception as e:
                    print(e)
                else:
                    break
            st2 = int(st2)
            st3 = int(st3)
            st1 = bytes(st1, encoding = 'utf-8')
            s = st.pack(form, st1 ,st2, st3)
            file.write(s) #Добавление в файл записи 

#Добавление записи в конец базы данных    
def Append(name, column):
    with open (name, 'a') as file:
        while True:
            try:
                st1 = input('Введите поле <Имя> записи: ')
                if not st1.isalpha():
                    raise Exception('В поле <Имя> должно быть введено одно слово!')
            except Exception as e:
                print(e)
            else:
                break
        while True:
            try:
                st2 = input('Введите поле <Возраст> записи: ')
                if not st2.isdigit():
                        raise Exception('В поле <Возраст> должно быть введено одно число!')    #Проверка на корректность введенных значений
            except Exception as e:
                print(e)
            else:
                break
        while True:
            try:
                st3 = input('Введите поле <Вес> записи: ')
                if not st3.isdigit():
                    raise Exception('В поле <Вес> должно быть введено одно число!')    #Проверка на корректность введенных значений
            except Exception as e:
                print(e)
            else:
                break
        file.write('{:^12}|{:^12}|{:^12}\n'.format(st1, st2, st3))

#Поиск по одному полю
def Find_c(name,column11, column1):
    ok = False
    with open (name, 'r') as file:
        while True:
            line = file.readline().strip('\n')
            if not line:
                break
            yes = False
            line1 = line.split('|')    #Разбиение записи по полям
            if column11 == 'Имя':
                ind = 0
            elif column11 == 'Возраст':
                ind = 1
            else:
                ind = 2
            x = line1[ind].split()
            if x[0] == column1:   #Проверка на сходство с искомым полем
                print('\nНайдена запись: ')
                print(line)
                ok = True
            
    if not ok:
        print('\nИскомой записи нет в базе данных.')



#Поиск по двум полям            
def Find_c2(name,column1, column2, ind11, ind22):
    ok = False
    with open (name, 'r') as file:
        while True:
            cnt1,cnt2 = 0, 0
            line = file.readline().strip('\n')
            if not line:
                break
            line1 = line.split('|')    #Разбиение записи по полям
            cnt1, cnt2 = 0, 0
            x = line1[ind11].split()
            x1 = x[0]
            if x1 == column1:
                cnt1 += 1
            x = line1[ind22].split()
            x2 = x[0]
            if x2 == column2:
                cnt2 += 1    
            if cnt1 == 1 and cnt2 == 1:    #Если оба слова хотя бы раз встретились в записи,то зарпись подходит
                print('\nНайдена запись: ')
                print(line)
                ok = True
    if not ok:
        print('\nИскомой записи нет в базе данных выбранного файла.')
                
n = None
name = None
file = None
column=['Имя','Возраст','Вес']
#form = "=cii" #"=10sii"
#Вывод меню
print('Меню: ')
print('1. Выбрать файл для работы.')
print('2. Инициализировать базу данных.')
print('3. Вывести содержимое базы данных.')
print('4. Добавить запись в произвольное место базы данных.')
print('5. Удалить произвольную запись из базы данных.')
print('6. Поиск по одному полю.')
print('7. Поиск по двум полям.')
print('0. Завершение работы меню.')

form = '=10sii'
#Ввод и проверка данных
while True:
    try:
        ok = True
        n = int(input('\nВведите одну из цифр 0 - 6: '))
        if (n < 0 or n > 6) and n != 0:
            ok = False
            raise Exception('Введена неверная цифра, попробуйте снова.')
    except  ValueError:
        ok = False
        print('Должна быть введена цифра!')
    except Exception as e:
        ok = False
        print(e)
    if ok:
        if n == 1:
            s = input('Введите имя файла с расширением: ')
            name = Choose(s, form)
            #Проверка на корректность введенного имени файла
            if name == None:
                print('Файл не существует.')
            elif name != s:
                print('Файл не подходит для выбора.')
                name = None
        elif n == 2:
            name1 = input('Введите имя файла с расширением или путь файла для создания: ')
            if os.path.exists(name1):
                print('\nТакой файл уже существует.')
                rewrite = input('Если хотите перезаписать его, то введите цифру 2, иначе введите любую другую цифру или символ: ')
                if rewrite == '2':
                    while True:
                        try:
                            m = int(input('Введите количесто записей базы данных: '))
                                #Проверка на корректность введенного числа записей
                            if m <= 0 or m != int(m):
                                raise Exception('Количество записей должно быть целым числом большим 0.')
                        except ValueError:
                            print('Должна быть введена цифра!')
                        except Exception as e:
                            print(e)
                        else:
                            break
                        #Инициализация базы данных
                    Base(name1, m, column, form)
            else:
                #Если файл не был выбран, то его необходимо выбрать
                c = 0
                while True:
                    if c > 0:
                        name1 = input('Введите имя файла с расширением ".bin" или путь файла для создания: ')
                    try:
                        if name1[-4:] != '.bin':
                            raise Exception
                        with open(name1, 'wb') as f:
                            pass
                    except:
                        print('Введенное файла не подходит.')
                        c += 1
                    else:
                        break
                while True:
                    try:
                        m = int(input('Введите количесто записей базы данных: '))
                            #Проверка на корректность введенного числа записей
                        if m < 0 or m != int(m):
                            raise Exception('Количество записей должно быть целым неотрицательным числом.')
                    except ValueError:
                        print('Должна быть введена цифра!')
                    except Exception as e:
                        print(e)
                    else:
                        break
                    #Инициализация базы данных
                Base(name1, m, column, form)
        if n == 3:
            #Если файл не был выбран, то его необходимо выбрать
            if name == None:
                print('Для выполнения дальнейших действий меню необходимо выбрать файл c помощью команды 1.')
            else:
                #Вывод содержимого базы данных
                print('\nСодержимое базы данных: ')
                with open(name, 'rb')as f:
                    s = f.read(st.calcsize(form))
                    s = st.unpack(form,s)
                    d = s[0].decode()
                    d1 = s[1]
                    d2 = s[2]
                    print('{:^10}'.format(d),end = '')
                    print('|{:^10}|{:^10}'.format(d1, d2))
            
        if n == 4:
            #Если файл не был выбран, то его необходимо выбрать
            if name == None:
                print('Для выполнения дальнейших действий меню необходимо выбрать файл c помощью команды 1.')
            else:
                #Добавление записи в конец 
                Append(name, column)
        if n == 5:
            #Если файл не был выбран, то его необходимо выбрать
            if name == None:
                print('Для выполнения дальнейших действий меню необходимо выбрать файл c помощью команды 1.')
            else:
                while True:
                    try:
                        column11 = input('Введите название поля, запись которого необходимо найти: ')
                        if column11 not in ['Имя', 'Возраст', 'Вес']:
                            raise Exception('Названием поля должно быть слово Имя, Возраст или Вес.')
                    except Exception as e:
                        print(e)
                    else:
                        break
                while True:
                    try:
                        column1 = input('Введите значение этого поля, запись которого необходимо найти: ')
                        if column1.count(' ') != 0 and ' ' * len(column1) != column1:
                            raise Exception('Значение поля не должно содержать пробелов.')
                    except Exception as e:
                        print(e)
                    else:
                        break
                #Поиск по полю
                Find_c(name, column11, column1)
        if n == 6:
            #Если файл не был выбран, то его необходимо выбрать
            if name == None:
                print('Для выполнения дальнейших действий меню необходимо выбрать файл c помощью команды 1.')
            else:
                while True:
                    try:
                        column11 = input('Введите название первого поля, запись которого необходимо найти: ')
                        if column11 not in ['Имя', 'Возраст', 'Вес'] :
                            raise Exception('Названием поля должно быть слово Имя, Возраст или Вес.')
                    except Exception as e:
                        print(e)
                    else:
                        break
                while True:
                    try:
                        column1 = input('Введите значение этого поля, запись которого необходимо найти: ')
                        if column1.count(' ') != 0 and ' ' * len(column1) != column1:
                            raise Exception('Значение поля не должно содержать пробелов.')
                    except Exception as e:
                        print(e)
                    else:
                        break
                while True:
                    try:
                        column22 = input('Введите название второго поля, запись которого необходимо найти: ')
                        if column22 not in ['Имя', 'Возраст', 'Вес'] or column11 == column22:
                            raise Exception('Названием второго поля не должно совпадать с выбранным ранее полем и должно быть слово Имя, Возраст или Вес.')
                    except Exception as e:
                        print(e)
                    else:
                        break
                while True:
                    try:
                        column2 = input('Введите значение этого поля, запись которого необходимо найти: ')
                        if column2.count(' ') != 0 and ' ' * len(column2) != column1:
                            raise Exception('Значение поля не должно содержать пробелов.')
                    except Exception as e:
                        print(e)
                    else:
                        break
                for i in range(3):
                    if column[i] == column11:
                        ind11 = i
                    elif column[i] == column22:
                        ind22 = i
                #Поиск по двум полям
                Find_c2(name, column1, column2, ind11, ind22)
        elif n == 0:
            print('Завершение работы меню.')
            break
