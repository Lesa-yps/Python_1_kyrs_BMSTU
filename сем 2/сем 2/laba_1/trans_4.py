# 10 -> 4
def trans_4(value1):
    if value1 == '': value1 = '0'

    res = ''

    if '.' in value1:
        num1, num2 = value1.split('.')
    else:
        num1 = value1
        num2 = '0'
    
    while int(num1) > 0:
        res = str(int(num1) % 4) + res
        num1 = str(int(num1) // 4)

    res += '.'

    num2 = '0.' + num2
    count = 0
    while float(num2) > 0 and count < 6:
        a = str(float(num2) * 4)
        res += str(a.split('.')[0])
        num2 = '0.' + str(a.split('.')[1])
        count += 1

    if res[0] == '.':
        res = '0' + res
    if res[-1] == '.':
        res += '0'

    return res
