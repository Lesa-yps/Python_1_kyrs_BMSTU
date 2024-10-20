# Сортирвка пузырьком строк в файле

with open('test.txt', 'w') as file:
    file.write('ddd\nw\nvv\nQ\nyouh\n')

##a = []
with open('test.txt', 'r') as file:
    for i in file:
        print(i, end = '')
    print()
##        a += [i]

##print(a)
##flag = True
##while flag:
##    flag = False
##    b_old = a[0]
##    for i in range(1, len(a)):
##            print(a[i-1], a[i])
##            input()
##            if len(a[i]) < len(a[i-1]):
##                flag = True
##                a[i], a[i - 1] = a[i - 1], a[i]
##                print('----------------')
##                print(a)
##                print('\n----------------')
                
with open('test.txt', 'r+') as file:
    flag = True
    while flag:
        flag = False
        file.seek(0)
        b_old = file.readline()
        while (b_new := file.readline()) != '':
            #print(b_old, b_new)
            #input()
            if len(b_new) < len(b_old):
                flag = True
                #print(file.tell(), len(b_new), len(b_old))
                file.seek(file.tell() - len(b_new) - 2 - len(b_old))
                #print(file.tell(), b_new + b_old)
                file.write(b_new + b_old)
                file.tell()
##                print('----------------')
##                with open('test.txt', 'r') as file1:
##                    for i in file1:
##                        print(i, end = '')
##                print('\n----------------')
            else:
                b_old = b_new


with open('test.txt', 'r') as file:
    for i in file:
        print(i, end = '')
                
