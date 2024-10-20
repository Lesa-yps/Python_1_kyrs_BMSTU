import struct as st
import time as ti
fmt = '<i'
los = st.calcsize(fmt)
with open('file.bin', 'wb') as file:
    a = lambda x: file.write(st.pack(fmt, x))
    for i in [241, 35, 745, -25, 0, 43515]:
        a(i)
    print('!', file.fileno())

def prin():
    with open('file.bin', 'rb') as file:
        k = 0
        while (b := file.read(los)) != b'':
            k += 1
            if k == 2:
                k = 0
                file.seek(- los, 1)
            print(st.unpack(fmt, b)[0])
        print('!', file.fileno())
        ti.sleep(2)
        file.flush()
        del k
prin()
with open('file.bin', 'r+b') as file:
    file.truncate(los * 3)
print('--------------')
print()
