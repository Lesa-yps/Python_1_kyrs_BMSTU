''' вводится имя файла в котором содержится текст текст разделён на предлож по символу .
вывести предложения в обатном порядке вводится
выходной файл в него записать проверку сущ для входного 1
записываем в 1 строке 1 предложение
считывать весь текст нельзя'''

f1 = None
while f1 == None:
    f1 = str(input('Введите путь к входному файлу: '))
    try:
        file1 = open(f1, 'r')
    except FileNotFoundError:
        print('Файл не найден. Повторите попытку.')
    except PermissionError:
        print('Права доступа к файлу ограничены. Повторите попытку.')
    except Exception:
        print('Ошибка открытия файла. Повторите попытку.')

f2 = str(input('Введите путь к выходному файлу: '))
file1.close()
file2 = open(f2, 'w')
file2.close()
file2 = open(f2, 'a+')
k = ''
flag = True
j = s = strk_last_1 = ''
while flag:
    flag = puf = False
    file1 = open(f1)
    strk = strk_last = ''
    for i in file1:
        for o in i:
                if o == '.':
                    strk += '.'
                    if strk != strk_last_1:
                        strk_last = strk
                        flag = True
                    else:
                        puf = True
                        break
                    strk = ''
                elif strk == '' and o == ' ':
                    pass
                else:
                    strk += o
        if puf:
            break
    file1.close()
    if strk_last != '':
        file2.write(strk_last.replace('\n', ' ') + '\n')
        strk_last_1 = strk_last
        strk_last = ''
file2.close()
