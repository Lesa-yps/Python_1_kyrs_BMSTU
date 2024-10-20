# Метод простых вставок

a = [213, 43, -23, 65, 0, 34, -2333, 4322]

for i in range(1, len(a)):
    j = i
    while a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1
        if j == 0:
            break

print(a)
