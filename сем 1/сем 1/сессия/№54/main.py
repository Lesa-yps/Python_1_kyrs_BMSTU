import numpy as np

# создание
a = np.array([1, 2, 3])
print(a)

print(np.zeros(2))
print(np.ones(3))
print(np.empty(5))
print(np.arange(4))
print(np.arange(2, 9, 2))
print(np.linspace(0, 10, num=5))

x = np.ones(2, dtype=np.int64)
print(x)

# сортировка
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

# соединение
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))

array_example = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]]])
print(array_example.ndim)  # количество измерений массива
print(array_example.size)  # количество элементов в массиве
print(array_example.shape)  # форма массива

# изменение формы
a = np.arange(6)
print(a)
b = a.reshape(3, 2)
print(b)
