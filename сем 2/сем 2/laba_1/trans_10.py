def trans_10(value2):
    if value2 == '': value2 = '0'

    res = '0'

    if '.' in value2:
        num1, num2 = value2.split('.')
    else:
        num1 = value2
        num2 = '0'

    k = 0
    while num1 != '':
        res = str(int(num1[0]) * 4**k + int(res))
        num1 = num1[:-1]
        k += 1

    res += '.'

    num2 = '0.' + num2
    count = 0
    k = -1
    while float(num2) > 0 and count < 6:
        print('!', res)
        res = str(float(num2[0]) * 4**k + float(res))
        print(res)
        num2 = num2[:2] + num2[3:]
        k -= 1
        count += 1

    if res[0] == '.':
        res = '0' + res
    if res[-1] == '.':
        res += '0'

    return res
