# Сортировка Шелла

a = [324, 43, 0, -23, 234, 21, -454, 34]

# шаг
pause = len(a) // 2

while pause > 0:
    for i in range(pause, len(a)):
        j = i
        while (j - pause) >= 0 and a[j] < a[j - pause]:
            a[j], a[j - pause] = a[j - pause], a[j]
            j -= pause
##            if (j - pause) < 0:
##                break
    pause //= 2

print(a)
