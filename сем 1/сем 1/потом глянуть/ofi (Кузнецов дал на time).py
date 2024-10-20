# Талышева ИУ7-15Б
# Программа, подключая модули array и time, сравнивает время работы вставки элемента
# удаления элемента, поиск по индексу и по значению в массивах и строках

import array as arr
import time as t

x_put, ind_put = 400000,5000000#map(int, input('Введите вставляемый элемент и его индекс через пробел: '))
ind_del = 5000000#int(input('Введите индекс удаляемого элемента: '))
ind_f = 5000000#int(input('Введите индекс искомого элемента: '))
x_f = 1000000#int(input('Введите искомый элемент: '))

print('   СПИСКИ')

a = [0] * 10000000
for i in range(10000000):
    a[i] = i

age = t.time()
a.insert(ind_put, x_put)
age_put_sp = t.time() - age
print('Время вставки:            ', age_put_sp)

age = t.time()
a.pop(ind_del)
age_del_sp = t.time() - age
print('Время удаления:           ', age_del_sp)

age = t.time()
b = a[ind_f]
age_ind_f_sp = t.time() - age
print('Время поиска по индексу:  ', age_ind_f_sp)

age = t.time()
for i in range(len(a)):
    if a[i] == x_f:
        age_x_f_sp = t.time() - age
        break
print('Время поиска по значению: ', age_x_f_sp)

print('   МАССИВЫ')

arr = [0] * 10000000
for i in range(10000000):
    arr[i] = i

age = t.time()
arr.insert(ind_put, x_put)
age_put_sp = t.time() - age
print('Время вставки:            ', age_put_sp)

age = t.time()
arr.pop(ind_del)
age_del_sp = t.time() - age
print('Время удаления:           ', age_del_sp)

age = t.time()
b = arr[ind_f]
age_ind_f_sp = t.time() - age
print('Время поиска по индексу:  ', age_ind_f_sp)

age = t.time()
b = arr.index(x_f)
age_x_f_sp = t.time() - age
print('Время поиска по значению: ', age_x_f_sp)



