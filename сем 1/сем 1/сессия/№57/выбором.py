# Сортировка выбором

a = [23, 0, 4132, -34, 232, 5]

for i in range(len(a) - 1):
    ind = a.index(min(a[i:]))
    a[i], a[ind] = a[ind], a[i]

print(a)
