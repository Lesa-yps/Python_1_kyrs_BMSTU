import tkinter as tk
import struct
from PIL import Image
from tkinter import ttk
# from tkinter import messagebox as mb

window = tk.Tk()
window.title("Stegenographia")
window.geometry("900x700")


# создаем рабочую область

label_path = tk.Label(text="Путь:")
label_path.grid(row=0, column=0)

path_txt = tk.Entry(window, width=30)  
path_txt.grid(row=0, column=1)  

label_txt = tk.Label(text="Текст:")
label_txt.grid(row=0, column=2)

txt = tk.Entry(window, width=30)  
txt.grid(row=0, column=3) 

l_txt = ttk.Label(text="Расшифрованное сообщение: ")
l_txt.grid(row=2, column=0)


# определяю, начинается ли число с 1 или 0
def get_bit(num: int, pos: int):
    return bool(num >> pos & 1)

# запись полученных из модуля decode чисел в конец байтов (стеганография)
def stegonography_txt(delta, bits, pack_data: bytes):
    b = 0
    tmp = list(bits[delta])
    for i in range(len(pack_data)):
        el_data = pack_data[i]
        for j in range(8):
            if get_bit(el_data, 7 - j):
                tmp[b % 3] |= 0x01
            else:
                tmp[b % 3] &= ~0x01
            b += 1
            if b % 3 == 0:
                bits[delta] = tuple(tmp)
                delta += 1
                tmp = list(bits[delta])
    else:
        bits[delta] = tuple(tmp)
    return bits

# получаю фотографию с декодированными байтами
def my_event_handler():
    pack_data = encoding()
    length = len(pack_data)
    pack_len = encoding_length(length)
    path = path_txt.get()
    img = Image.open(path)
    bits = list(img.getdata())
    bit = stegonography_txt(0, bits, pack_len)
    bitts = stegonography_txt(12, bit, pack_data)
    print(bitts[:10])
    img.putdata(bitts)
    img.save(path)

    img.show()

# кодирую введенное сообщение в байты
def encoding():
    text = txt.get()
    data = (text.encode('utf-8'))

    s = struct.Struct(str(len(data))+'s')
    pack_date = s.pack(data) 
    return pack_date

def encoding_length(l):
    pack_date = struct.pack('1i', l)
    return pack_date


def decoding_len(bits):
    place_lenth = ''
    for i in range(11):
        for j in range(3):
            el_data = bits[i][j]
            if get_bit(el_data, 0):
                place_lenth += "1"
            else:
                place_lenth += "0"
    place_lenth = place_lenth[0:32]

    dec = int(place_lenth, 2)
    byte = dec.to_bytes(4, byteorder="big")
    pl = struct.unpack('1i', byte)
    return (pl[0])

def handler_decode():
    decoding_all()

def decoding_all(bits = None):
    if bits is None:
        path = path_txt.get()
        img = Image.open(path)
        bits = list(img.getdata())
    lenth = decoding_len(bits)
    text = ''
    
    cur = 12 * 3
    bit = 0
    while cur < lenth * 8 + 12 * 3:
        tup = int(cur / 3)
        bit = cur % 3
        el_data = bits[tup][bit]
        if get_bit(el_data, 0):
            text += "1"
        else:
            text += "0"
        cur += 1
  
    arr = []
    for i in range(lenth):
        start = i * 8
        finish = i * 8 + 8
        s = text[start:finish]
        arr.append(int(s, 2).to_bytes(1, byteorder='big'))


    byte = (struct.unpack(str(lenth)+'s', b''.join(arr))[0])
    bytes = byte.decode('utf-8')
    decod_text = ttk.Label(text=bytes)
    decod_text.grid(row=2, column=1)


but = tk.Button(text="Зашифровать", command=my_event_handler).grid(row=1, column=0)

but1 = tk.Button(text="Расшифровать", command=handler_decode).grid(row=1, column=1)



# l1 = tk.Label(decoding_all, font="Arial 32").grid(row=2, column=1)

window.mainloop()
