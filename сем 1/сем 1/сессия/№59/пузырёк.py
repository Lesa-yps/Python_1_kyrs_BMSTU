# Сортировка пузырьком
a = [342, 54, 2, -67, 90, 6, -435, 0, 45, 7, 1]

for i in range(len(a) - 1):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]

print(a)
