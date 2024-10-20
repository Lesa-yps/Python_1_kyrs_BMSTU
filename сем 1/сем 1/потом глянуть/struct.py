Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import struct as s
s = pack('<sisf', 'D',23,'зачет',17238)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s = pack('<sisf', 'D',23,'зачет',17238)
NameError: name 'pack' is not defined
import struct as st
s = st.pack('<sisf', 'D',23,'зачет',17238)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s = st.pack('<sisf', 'D',23,'зачет',17238)
struct.error: argument for 's' must be a bytes object
s = st.pack('<if',23,17238)
s
b'\x17\x00\x00\x00\x00\xac\x86F'
s = st.pack('<sif','Ivanov',23,17238)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s = st.pack('<sif','Ivanov',23,17238)
struct.error: argument for 's' must be a bytes object
s = st.pack('<sif',b'Ivanov',23,17238)
s
b'I\x17\x00\x00\x00\x00\xac\x86F'
s = st.pack('<sif',b'Иванов',23,17238)
SyntaxError: bytes can only contain ASCII literal characters
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<sisf',b'Иванов',23,b'offset',17238)
    
SyntaxError: bytes can only contain ASCII literal characters
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<sisf',b'Ivanov',23,b'offset',17238)
    s = st.pack('<sisf',b'Shyrov',87,b'fail',1723)

    
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<sisf',b'Ivanov',23,b'offset',17238)
    file.write(s)
    s = st.pack('<sisf',b'Shyrov',87,b'fail',1723)
    file.write(s)

    
10
10
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    for i in file:
        s = st.unpack('<sisf',i)
        print(s)

        
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    for i in file:
io.UnsupportedOperation: read
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.unpack('<sisf',file)
    print(s)

    
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    s = st.unpack('<sisf',file)
TypeError: a bytes-like object is required, not '_io.BufferedWriter'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<sisf',b'Ivanov',23,b'offset',17238)
    file.write(s)
    s = st.pack('<sisf',b'Shyrov',87,b'fail',1723)
    file.write(s)

    
10
10
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    s = unpack('<sisf', file)
    print(s)

    
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    s = unpack('<sisf', file)
NameError: name 'unpack' is not defined
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    s = st.unpack('<sisf', file)
    print(s)

    
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    s = st.unpack('<sisf', file)
TypeError: a bytes-like object is required, not '_io.BufferedReader'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<sisf', s)
        print(s1)

        
(b'I', 23, b'o', 17238.0)
(b'S', 87, b'f', 1723.0)
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<sisf', s)
        a = s1[0]
        print(s1, a)

        
(b'I', 23, b'o', 17238.0) b'I'
(b'S', 87, b'f', 1723.0) b'S'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<sisf',b'Ivanov',23,b'offset',17238)
    file.write(s)
    s = st.pack('<sisf',b'Shyrov',87,b'fail',1723)
    file.write(s)

    
10
10
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<sisf', s)
        a = s1[0]
        print(s1, a)

        
(b'I', 23, b'o', 17238.0) b'I'
(b'S', 87, b'f', 1723.0) b'S'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<sisf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
(b'I', 23, b'o', 17238.0) 'I'
(b'S', 87, b'f', 1723.0) 'S'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<6si6sf',b'Ivanov',23,b'offset',17238)
    file.write(s)
    s = st.pack('<sisf',b'Shyrov',87,b'fail',1723)
    file.write(s)

    
20
10
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<6si6sf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
Traceback (most recent call last):
  File "<pyshell#43>", line 3, in <module>
    s1 = st.unpack('<6si6sf', s)
struct.error: unpack requires a buffer of 20 bytes
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<6si6sf',b'Ivanov',23,b'offset',17238)
    file.write(s)
    s = st.pack('<6si6sf',b'Shyrov',87,b'fail',1723)
    file.write(s)

    
20
20
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<6si6sf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
Traceback (most recent call last):
  File "<pyshell#47>", line 3, in <module>
    s1 = st.unpack('<6si6sf', s)
struct.error: unpack requires a buffer of 20 bytes
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<6si6sf')):
        s1 = st.unpack('<6si6sf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
(b'Ivanov', 23, b'offset', 17238.0) 'Ivanov'
(b'Shyrov', 87, b'fail\x00\x00', 1723.0) 'Shyrov'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<sisf')):
        s1 = st.unpack('<10si10sf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
Traceback (most recent call last):
  File "<pyshell#51>", line 3, in <module>
    s1 = st.unpack('<10si10sf', s)
struct.error: unpack requires a buffer of 28 bytes
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'wb') as file:
    s = st.pack('<10si6sf',b'Ivanov',23,b'offset',17238)
    file.write(s)
    s = st.pack('<10si6sf',b'Shyrov',87,b'fail',1723)
    file.write(s)

    
24
24
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<10si6sf')):
        s1 = st.unpack('<10si6sf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
(b'Ivanov\x00\x00\x00\x00', 23, b'offset', 17238.0) 'Ivanov\x00\x00\x00\x00'
(b'Shyrov\x00\x00\x00\x00', 87, b'fail\x00\x00', 1723.0) 'Shyrov\x00\x00\x00\x00'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<10si6sf')):
        s1 = st.unpack('<10si6sf', s)
        a = str(s1[0])[1:s1[0].find("\x")]
        print(s1, a)
        
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-1: truncated \xXX escape
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<10si6sf')):
        s1 = st.unpack('<10si6sf', s)
        a = str(s1[0])[1:str(s1[0]).find("\x")]
        print(s1, a)
        
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-1: truncated \xXX escape
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<10si6sf')):
        s1 = st.unpack('<10si6sf', s)
        a = str(s1[0])[1:]
        print(s1, a)

        
(b'Ivanov\x00\x00\x00\x00', 23, b'offset', 17238.0) 'Ivanov\x00\x00\x00\x00'
(b'Shyrov\x00\x00\x00\x00', 87, b'fail\x00\x00', 1723.0) 'Shyrov\x00\x00\x00\x00'
with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
    while s := file.read(st.calcsize('<10si6sf')):
...         s1 = st.unpack('<10si6sf', s)
...         a = str(s1[0])[1:str(s1[0]).find('\x00')]
...         print(s1, a)
... 
...         
(b'Ivanov\x00\x00\x00\x00', 23, b'offset', 17238.0) 'Ivanov\x00\x00\x00\x00
(b'Shyrov\x00\x00\x00\x00', 87, b'fail\x00\x00', 1723.0) 'Shyrov\x00\x00\x00\x00
>>> with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
...     while s := file.read(st.calcsize('<10si6sf')):
...         s1 = st.unpack('<10si6sf', s)
...         a = str(s1[0])[1:str(s1[0]).find('0') - 3]
...         print(s1, a)
... 
...         
(b'Ivanov\x00\x00\x00\x00', 23, b'offset', 17238.0) 'Ivano
(b'Shyrov\x00\x00\x00\x00', 87, b'fail\x00\x00', 1723.0) 'Shyro
>>> with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
...     while s := file.read(st.calcsize('<10si6sf')):
...         s1 = st.unpack('<10si6sf', s)
...         a = str(s1[0])[1:str(s1[0]).find('0') - 2]
...         print(s1, a)
... 
...         
(b'Ivanov\x00\x00\x00\x00', 23, b'offset', 17238.0) 'Ivanov
(b'Shyrov\x00\x00\x00\x00', 87, b'fail\x00\x00', 1723.0) 'Shyrov
>>> 1with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
...     while s := file.read(st.calcsize('<10si6sf')):
...         s1 = st.unpack('<10si6sf', s)
...         a = str(s1[0])[2:str(s1[0]).find('0') - 2]
...         print(s1, a)
...         
SyntaxError: invalid decimal literal
>>> with open('F:\учеба\Бауманка Python\БД (лаба 14_BIN)\e.txt', 'rb') as file:
...     while s := file.read(st.calcsize('<10si6sf')):
...         s1 = st.unpack('<10si6sf', s)
...         a = str(s1[0])[2:str(s1[0]).find('0') - 2]
...         print(s1, a)
... 
...         
(b'Ivanov\x00\x00\x00\x00', 23, b'offset', 17238.0) Ivanov
(b'Shyrov\x00\x00\x00\x00', 87, b'fail\x00\x00', 1723.0) Shyrov
