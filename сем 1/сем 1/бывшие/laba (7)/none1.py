# Тадышева ИУ7-15Б
# Программа удаляет все положительные элементы из введённого списка

# Ввод массива
a = [i for i in map(int, input('Введите элементы массива через пробел: ').split())]
# Задаем счётчик индекса
i = 0
# Пока счётчик индекса меньше длины массива цикл выполняется
while i < len(a):
    # Если текущий элемент положительный, удаляем его и счетчик индекса уменьшаем на 1
    if a[i] > 0:
        a.pop(i)
        i -= 1
    # Счётчик индекса увеличиваем на 1
    i += 1
# Вывод массива
if len(a) == 0:
    print('Массив пуст')
else:
    print('Итоговый массив: ', a)
