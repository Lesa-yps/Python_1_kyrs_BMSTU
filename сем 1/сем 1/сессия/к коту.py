with open('кот.bin', 'r+b') as file:
    m = file.read(10)
    print(m)
    
    k = 'ущ55злрнзщ5'.encode('utf-8')
    file.write(k)
    print(k)
