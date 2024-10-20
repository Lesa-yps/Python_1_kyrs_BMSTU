# Сортирвка вставками

a = [342, 54, 2, -67, 90, 6, -435, 0, 45, 7, 1]

for i in range(1, len(a)):
    j = i
    print(a[i])
    while a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1
        if j <= 0:
            break
    print(a)

print(a)
