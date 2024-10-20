from PIL import Image as Im
from Check import *

def get_shifr(img_list):
    strk = ''
    simbol = ''
    i = 0
    while True:
        if len(simbol) == MAX_LEN:
            strk += chr(int(simbol, 2))
            simbol = ''
            if strk[-1] == '~':
                break
        simbol += str(img_list[i][2])
        i += 1
    return strk[:-1]

def antishifr(way):
    if checker(way, "финиш"):
        return 1
    img = Im.open(way)
    img_list = list(img.getdata())
    img.close()
    strk = get_shifr(img_list)
    return strk
    
