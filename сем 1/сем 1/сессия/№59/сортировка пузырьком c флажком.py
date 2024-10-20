# Сортировка пузырьком с флагом

a = [213, 43, -23, 65, 0, 34, -2333, 4322]

for i in range(len(a) - 1):
    flag = False
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = True
    if not flag:
        break

print(a)
