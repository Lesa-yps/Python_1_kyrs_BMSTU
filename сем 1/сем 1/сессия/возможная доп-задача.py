# Запишет числа в файл в бинарном виде и выведет только чётные
import struct as st
fmt = '<i'
los = st.calcsize(fmt)

n = None
while n == None:
    try:
        n = int(input('Введите количество чисел, которые необходимо записать в файл: '))
    except ValueError:
        print('Ошибка: ведённое значение должно быть целым числом. Повторите попытку.')
    except Exception as e:
        print('Ошибка:', e, 'Повторите попытку.')
    else:
        if n <= 0:
            print('Количество неположительное: файл будет очищен')

f = None
while f == None:
    try:
        f = input('Введите путь к файлу, в который необходимо записать числа: ')
        if f == '':
            print('Ошибка: введена пустая строка Повторите попытку.')
            f = None
        else:
            file = open(f, 'wb')
            file.close()
    except PermissionError:
        print('Ошибка доступа к файлу. Повторите попытку выбора файла.')
        f = None
    except Exception as e:
        print('Ошибка:', e)
        f = None
    else:
        if n > 0:
            print('Файл для работы выбран')
        else:
            print('Файл очищен')

with open(f, 'wb') as file:
    for _ in range(n):
        x = None
        while x == None:
            try:
                x = int(input('Введите число №{}, которое необходимо записать в файл: '.format(_ + 1)))
            except ValueError:
                print('Ошибка: ведённое значение должно быть целым числом. Повторите попытку.')
            except Exception as e:
                print('Ошибка:', e, 'Повторите попытку.')
        x = st.pack(fmt, x)
        file.write(x)
    if n > 0:
        print('Числа записаны ^-^')

flag = False
with open(f, 'rb') as file:
    for _ in range(n):
        x = file.read(los)
        x = st.unpack(fmt, x)[0]
        if x % 2 == 0:
            if not flag:
                print('Чётные числа из файла:')
                flag = True
            print(x)
if not flag and n > 0:
    print('Чётных чисел в файле нет')
