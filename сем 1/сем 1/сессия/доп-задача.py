import struct as st
fmt = '<i'
los = st.calcsize(fmt)

n = int(input('Введите количество чисел: '))
f = input('Введите путь к файлу: ')

with open(f, 'wb') as file:
    for _ in range(n):
        x = int(input('Введите число №{}: '.format(_ + 1)))
        x = st.pack(fmt, x)
        file.write(x)
print('Числа записаны')

flag = False
with open(f, 'rb') as file:
    for _ in range(n):
        x = file.read(los)
        x = st.unpack(fmt, x)[0]
        if x % 2 == 0:
            if not flag:
                print('Чётные числа в файле:')
                flag = True
            print(x)
if not flag:
    print('Чётных чисел в файле нет.')
