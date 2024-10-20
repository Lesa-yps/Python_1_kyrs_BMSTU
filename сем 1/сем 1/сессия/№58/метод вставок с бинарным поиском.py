# Метод вставок с бинарным поиском

a = [213, 43, -23, 65, 0, 34, -2333, 4322]

# как во вставках простых цикл начинаем со второго элемента и до конца
for i in range(1, len(a)):
    # левая граница
    left = 0
    # включаем правую границу
    right = i
    # Пока границы в правильном порядке и не сошлись
    while right > left:
        # Обновляем индекс центрального элемента в зависимости от новых границ
        center = (left + right) // 2
        # если текущий элемент меньше цнтрального смещаем правую гграницу
        if a[i] < a[center]:
            right = center - 1
        # если текущий элемент больше цнтрального смещаем левую гграницу
        elif a[i] > a[center]:
            left = center + 1
        # если текущий элемент равен цнтральному - это нужное место,
        # сравниваем границы с центральным, чтобы выйти из цикла
        else:
            left = right = center
    # вставляем элемент на место левой границы (так как деление целочисленное в меньшую сторону)
    # и удаляем его на старом месте
    a.insert(left, a[i])
    a.pop(i+1)

print(a)
        
            
        
        
