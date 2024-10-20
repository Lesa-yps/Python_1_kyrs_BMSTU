# Талышева ИУ7-15Б
a = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
if len(a) == 0 or len(a) == 1:
    print('Второго по величине элемента нет')
else:
    maxi1 = a[0]
    maxi2 = -10**10
    for i in range(1, len(a)):
        if a[i] > maxi1:
            maxi2 = maxi1
            maxi1 = a[i]
        elif a[i] > maxi2 and a[i] != maxi1:
            maxi2 = a[i]
    if maxi2 == -10**10:
        print('Второго по величине элемента нет')
    else:
        print('Второе по величине число: ', maxi2)
    
