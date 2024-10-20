# Тадышева ИУ7-15Б
# Программа находит самый короткую строку, не содержащую пробелов, в введенном массиве

# Ввод массива
a = [i for i in input('Введите элементы массива через запятую: ').split(',')]
# Проходимся по массиву и проверяем существует ли строка, не содержащая пробел, в массиве
# Если существует - запоминаем её индекс в переменную mini
flag = False
for i in range(len(a)):
    if ' ' not in a[i]:
        mini = i
        flag = True
        break
# Если строки, не содержащей пробела, нет в массиве, программа выводит, что такой строки нет
if not flag:
    print ('Строки без пробелов нет')
else:
    # Проверяем список на наличие элементов
    if len(a) == 1 and a[0] == '':
            print('Массив пуст')
    # Если подходящая строка последняя, выводим её
    elif mini == (len(a) - 1):
        print('Самая короткая строка, не содержащая пробелов: ', a[mini])
    # Иначе проходимся по списку
    else:
        for i in range(mini + 1, len(a)):
            # Если текущий элемент не содержит пробела и он короче минимальной подходящей строки
            # Запоминаем индекс элемента
            if ' ' not in a[i] and len(a[i]) < len(a[mini]):
                mini = i
        # Вывод массива
        print('Самая короткая строка, не содержащая пробелов: ', a[mini])
