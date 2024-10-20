# Сортировка пузырьком

#a = [213, 43, -23, 65, 0, 34, -2333, 4322]
a = [i for i in range(5, -1, -1)]

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
