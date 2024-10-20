# Метод всавок с барьером

a = [213, 43, -23, 65, 0, 34, -2333, 4322]

for i in range(1, len(a)):
    a.insert(0, a[i])
    #a = [a[i]] + a
    #a = a[i:i + 1] + a
    j = i + 1
    while a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1
    #a = a[1:]
    a.pop(0)

print(a)
