# Метод Шейкер сортировки

a = [213, 43, -23, 65, 0, 34, -2333, 4322]

for i in range(len(a) - 1):
    for j in range(i, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    for k in range(j, 0, -1):
        if a[k] < a[k - 1]:
            a[k], a[k - 1] = a[k - 1], a[k]

print(a)
