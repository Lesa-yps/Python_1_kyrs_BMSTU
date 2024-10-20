# решетка Кардано
# программа шифрует строку <= 64 символов
from time import sleep
from random import randint, choice
from string import ascii_letters

# Функция выберет файлы для работы
def Choose_Files():
    f = None
    while f == None:
        f = str(input('Введите путь к файлу без префикса: '))
        if f == '':
             f = None
             print('Введена пустая строка. Повторите попытку.')
        else:
            f_key = f + 'key.txt'
            f_mat = f + 'matrix.txt'
            try:
                key = open(f_key, 'a')
                mat = open(f_mat, 'a')
            except PermissionError:
                print('Ошибка доступа. Повторите попытку.')
                f = None
            except Exception:
                print('Ошибка открытия файла. Повторите попытку.')
                f = None
            else:
                print('Файлы для работы выбраны.')
                key.close()
                mat.close()
    return f_key, f_mat

''' ЗАШИФРОВКА '''

def Create_Matrix():
    M = [[0] * 8 for i in range(8)]
    for i in range(4):
        for j in range(4):
            M[i][j] = i * 4 + j + 1
            M[j][7 - i] = i * 4 + j + 1
            M[7 - i][7 - j] = i * 4 + j + 1
            M[7 - j][i] = i * 4 + j + 1
    for i in range(1, 17):
        q = randint(1, 4)
        i -= 1
        if q == 1:
            M[i // 4][i % 4] = '0'
            M[i % 4][7 - i // 4] = '1'
            M[7 - i // 4][7 - i % 4] = '1'
            M[7 - i % 4][i // 4] = '1'
        elif q == 2:
            M[i % 4][7 - i // 4] = '0'
            M[i // 4][i % 4] = '1'
            M[7 - i // 4][7 - i % 4] = '1'
            M[7 - i % 4][i // 4] = '1'
        elif q == 3:
            M[7 - i // 4][7 - i % 4] = '0'
            M[i // 4][i % 4] = '1'
            M[i % 4][7 - i // 4] = '1'
            M[7 - i % 4][i // 4] = '1'
        elif q == 4:
            M[7 - i % 4][i // 4] = '0'
            M[i // 4][i % 4] = '1'
            M[i % 4][7 - i // 4] = '1'
            M[7 - i // 4][7 - i % 4] = '1'
    A = [0] * 8
    for i in range(8):
        A[i] = str(int('?'.join(M[i]).replace('?', ''), 2)) + '\n'
    fk, fm = Choose_Files()
    with open(fk, 'w') as f:
        for i in range(8):
            f.write(A[i])
    return M, fm

# Функция считает строку, которую нужно зашифровать
def Strka():
    strk = str(input('Диктуйте строку, Холмс! (макс длина = 64, дальше - обрежется, меньше дополнится рандомно, конец строки - "#")\n: '))
    if len(strk) > 64:
        print('Примечание для особо одарённых (*!*): строка обрежется)')
    else:
        strk += '#'
        while len(strk) < 64:
            strk += choice(ascii_letters)
        print('Строка была дополнена. Ну, так, на всякий случай) Вдруг ты успел(а) забыть ^+^')
    return strk

# Функция зашифрует строку и запишет в файл
def Chifr(strk, fm):
    Q = [[0] * 8 for i in range(8)]
    for k in range(4):
        for i in range(8):
            for j in range(8):
                if M[i][j] == '0':
                    Q[i][j] = strk[0]
                    strk = strk[1:]
        if k != 3:
            for i in range(4):
                for j in range(4):
                    M[j][7 - i], M[7 - i][7 - j], M[7 - j][i], M[i][j] = M[i][j], M[j][7 - i], M[7 - i][7 - j], M[7 - j][i]
    with open(fm, 'w') as f:
        for i in range(8):
           f.write('?'.join(Q[i]).replace('?', '') + '\n')
                    
n = None
while n != 0:
    try:
        n = int(input('\nВведите действие, которое необходимо совершить:\n\
    0) выйти из программы\n\
    1) зашифровать строку (<= 64 симоволов)\n\
    2) расшифровать строку из матрицы\n: '))
        print()
    except ValueError:
        print('Ты дура(к)? Введи ЦЕЛОЕ ЧИСЛО!')
    except Exception:
        print('Я не знаю что за ошибку ты вызвал, но цензурных слов у меня нет. Измени ввод, поль...рак!')
    else:
        if n == 0:
            print('ТОчно? ^-^')
            sleep(2)
            print('Блииин, ну ладно...')
        elif n == 1:
            print('Шифровальщик включён. #+#')
            # Запишет ключ и получит имена файлов и адекватную матрицу (0/1)
            M, fm = Create_Matrix()
            # Считывание строки, которую нужно зашифровать
            strk = Strka()
            # Зашифрует строку и запишет в файл
            Chifr(strk, fm)
            print('Я записал ^*^ Кто молодец?')
            sleep(1.2)
            print('Я молодец! ^:^')
        elif n == 2:
            print('ОK @~@', end = ' ')
        else:
            print('Ты %#@&*? Такого номера нет! Перечитай задание! ВНИМАТЕЛЬНО -_-')
            
