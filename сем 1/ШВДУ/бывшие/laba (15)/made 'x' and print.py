import struct as st
fmt = '<i'
with open('x.bin', 'wb') as f:
    s = st.pack(fmt, -324)
    f.write(s)
    s = st.pack(fmt, 98)
    f.write(s)
    s = st.pack(fmt, -1)
    f.write(s)
    s = st.pack(fmt, 566788)
    f.write(s)
    s = st.pack(fmt, 326)
    f.write(s)
    s = st.pack(fmt, 12)
    f.write(s)
    s = st.pack(fmt, -8790)
    f.write(s)
    s = st.pack(fmt, -34)
    f.write(s)
    s = st.pack(fmt, 121)
    f.write(s)
    s = st.pack(fmt, 0)
    f.write(s)
with open('x.bin', 'rb') as f:
    while s1 := f.read(st.calcsize(fmt)):
        s = st.unpack(fmt, s1)
        print(s)
