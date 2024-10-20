
import time as t
import random as r
EPS = 10**-8

def sheaker(a, size):
    l = 0
    r = size - 1

    while l <= r:
        for i in range(l, r):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        r -= 1
        for i in range(r, l, -1):
            if a[i-1] > a[i]:
                a[i], a[i-1]=a[i-1], a[i]
        l += 1


def heapify(arr, size, root): #  Преобразование массива в двоичную кучу
    largest = root #  Индекс наибольшего элемента
    l = 2 * root + 1 # Индекс левого дочернего элемента
    r = 2 * root + 2 # Индекс правого дочернего элемента

    if l < size and arr[l] > arr[largest]: #  Присваивание индекса наибольшего элемента
        largest = l

    if r < size and arr[r] > arr[largest]: #  Присваивание индекса наибольшего элемента  
        largest = r
    
    if root != largest: #  Если это не конечный элемент дерева
        arr[largest], arr[root] = arr[root], arr[largest] #  swap наибольшего дочернего элемента с корнем
        heapify(arr, size, largest) #  Преобразование изменённого массива в двоичную кучу


def build_heap(arr, size): #  Создание из массива двоичной кучи
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i) #  Преобразование массива в двоичную кучу

def heap_sort(arr, size): #  Пирамидальная сортировка
    build_heap(arr, size) #  Построение двоичной кучи из массива
    
    for i in range(size - 1, -1, -1): #  Сортировка кучи
        arr[0], arr[i] = arr[i], arr[0] #  Замена наибольшего элемента кучи на конечный
        heapify(arr, i , 0) #  Преобразование уменьшеного дерева в двоичную кучу


def binary_insert(arr, size):
    for i in range(size):
        key = arr[i]
        lo, hi = 0, i - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > key:
                hi = mid
            else:
                lo = mid + 1
        
        for j in range(i, lo + 1, -1):
            arr[j] = arr[j - 1]
        arr[lo] = key


def shell_sort(arr, size):
    step = size // 2
    while step > 0:
        for i in range(step, size):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step
        step //= 2


def bubble_sort_flag(arr, size):
    flag = True
    while flag:
        flag = False
        for j in range(size - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True


def insert_sort(arr, size):
    for i in range(size):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr, size):
    for i in range(0, size):
        mn = i
        for j in range(i + 1, size):
            if arr[mn] > arr[j]:
                mn = j
        arr[mn], arr[i] = arr[i], arr[mn]


def comb_sort(arr, size):
    step = int(size / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < size:
            if arr[i] > arr[i+step]:
                arr[i], arr[i+step] = arr[i+step], arr[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)
    

def insert_barrier_sort(a, size):

    arr = [0] + a

    for i in range(2, size + 1):
        if arr[i - 1] > arr[i]:
            arr[0] = arr[i]
            j = i - 1
            while (arr[j] > arr[0]) and (j > 0):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = arr[0]
    #return arr[1:]

def gnome_sort(arr, size):
    i = 1
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1



n = int(input("Count >> "))

arr = [r.randint(-100, 100) for i in range(n)]
temp = arr.copy()

start_time = t.time() #  Время начала сортировки
sheaker(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Шейкер: {end_time - start_time}")


arr = temp.copy()
start_time = t.time() #  Время начала сортировк
heap_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Heap sort: {end_time - start_time}")


arr = temp.copy()
start_time = t.time() #  Время начала сортировк
binary_insert(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Бинарные вставки: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
shell_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Сортировка Шелла: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
bubble_sort_flag(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Сортировка пузырьком с флагом: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
insert_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Сортировка простыми вставками: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
selection_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Сортировка простым выбором: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
comb_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Сортировка расчёской: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
insert_barrier_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Сортировка вставками с барьером: {end_time - start_time}")

arr = temp.copy()
start_time = t.time() #  Время начала сортировк
gnome_sort(arr, n)
end_time = t.time() #  Время конца сортировка
print(f"Гномья сортировка: {end_time - start_time}")