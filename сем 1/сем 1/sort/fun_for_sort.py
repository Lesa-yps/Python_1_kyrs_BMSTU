x = [4, 2, -1, 0, 5, 1, 3]

# Простым выбором
##def Srt(x):
##    k = 0
##    for i in range(len(x)):
##        num = x.index(min(x[k:]))
##        x[k], x[num] = x[num], x[k]
##        k += 1
##    return x

# фигня какая-то
##def Srt(x):
##    for i in range(len(x)):
##        for j in range(i+1, len(x)):
##            if x[i] > x[j]:
##                x[i], x[j] = x[j], x[i]
##    return x

### Пузырьком
##def Srt(x):
##    for i in range(len(x) - 1):
##        for j in range(1, len(x) - i):
##            if x[j] < x[j - 1]:
##                x[j - 1], x[j] = x[j], x[j - 1]
##    return x


### Пузырьком c флагом
##def Srt(x):
##    for i in range(len(x) - 1):
##        flag = False
##        for j in range(1, len(x) - i):
##            if x[j] < x[j - 1]:
##                x[j - 1], x[j] = x[j], x[j - 1]
##                flag = True
##        if not flag:
##            break
##    return x

### Шейкер
##def Srt(x):
##    for i in range(len(x) - 1):
##        flag = False
##        for j in range(i, len(x) - i):
##            if x[j] < x[j - 1]:
##                x[j - 1], x[j] = x[j], x[j - 1]
##                flag = True
##        for j in range(i, len(x) - i - 1, -1):
##            if x[j] < x[j - 1]:
##                x[j - 1], x[j] = x[j], x[j - 1]
##                flag = True
##        if not flag:
##            break
##    return x

# Простыми вставками
##def Srt(x):
##    m = 0
##    while m + 1 < len(x):
##        m += 1
##        k = m
##        while x[k] < x[k - 1]:
##            x[k], x[k - 1] = x[k - 1], x[k]
##            k -= 1
##            if (k - 1) < 0:
##                break
##    return x

# Вставками с барьером
##def Srt(x):
##    m = 1
##    while m < len(x):
##        x = [0] + x
##        m += 1
##        k = m
##        x[0] = x[k]
##        while x[k] < x[k - 1]:
##            x[k], x[k - 1] = x[k - 1], x[k]
##            k -= 1
##        x = x[1:]
##    return x

print(Srt(x))
