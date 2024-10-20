# сортирока вставками

a = [23, 0, 4132, -34, 232, 5]

for i in range(1, len(a)):
    j = i
    while a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1
        if j == 0:
            break

print(a)
