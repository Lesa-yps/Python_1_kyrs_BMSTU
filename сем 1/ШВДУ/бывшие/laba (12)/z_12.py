# rнайти предлож в которо встеч выражение значение которого после вычисл четно + - удалить предлож наименьшей длины .!? неодин
s = ['   Когда он разговаривал с ней таким образом, вдруг загремела музыка. Каштанка оглянулась ',
    'и увидела, что по улице прямо на неё  шёл полк 800 - 2 солдат. Не вынося музыки, ',
    'которая расстраивала ей нервы, она заметалась и завыла. К великому её удивлению,',
    'столяр, вместо того, чтобы испугаться, завизжать и залаять, широко ',
    'улыбнулся, вытянулся во фрунт и всей 3+2 сделал под козырек. Видя, что хозяин ',
    'не протестует, Каштанка еще громче завыла и, не помня себя, ',
    'бросилась через дорогу на другой тротуар. Когда ',
    'она опомнилась, музыка уже не играла и полка не было.']

def s_to_line(s):
    line = ''
    for i in range(len(s)):
        line +=  s[i] + '&'
    return line

def line_to_s(line):
    for i in range(len(s)):
        s[i] = line[:(line.find('&'))]
        line = line[(line.find('&') + 1):]
    return s

line = s_to_line(s)
win = False
mig = True
while mig:
    mig = False
    j = 0
    while j < len(line): 
        if line[j] in '+-':
            qz = 0
            strk1 = strk2 = ''
            count1 = count2 = j
            basta = puf = False
            for k in range(j - 1, -1, -1):
                    if line[k].isdigit():
                            if not puf:
                                    strk1 = line[k] + strk1
                                    count1 = k
                                    basta = True
                            elif puf:
                                    break
                    elif not basta:
                            if line[k] in ' )&':
                                    if line[k] == '&':
                                            qz += 1
                            else:
                                    break
                    elif basta:
                                puf = True
                                if line[k] in ' (':
                                        pass
                                elif line[k] == '-' and strk1[0] == '-':
                                        strk1 = strk1[1:]
                                        count1 = k
                                elif line[k] == '-' and strk1[0] != '-':
                                        strk1 = '-' + strk1
                                        count1 = k
                                else:
                                        break                
            basta = False
            for k in range(j + 1, len(line)):
                        if line[k].isdigit():
                                strk2 += line[k]
                                count2 = k
                                basta = True
                        elif not basta:
                                if line[k] in ' (&':
                                        if line[k] == '&':
                                                qz += 1
                                elif line[k] == '-' and strk2 == '':
                                        strk2 = '-'
                                elif line[k] == '-' and strk2 == '-':
                                        strk2 = ''
                                else:
                                        break
                        elif basta:
                                break
            if strk1 != '' and strk2 != '-' and strk2 != '':
                    mig = True
                    if line[j] == '+':
                        strk = int(strk1) + int(strk2)
                    elif line[j] == '-':
                        strk = int(strk1) - int(strk2)
                    line = line[:count1] + str(strk) + '&' * qz + line[(count2 + 1):]
                    j = count1 + len(str(strk) + '&' * qz) - 1
                    if strk % 2 == 0:
                        st = 0
                        fi = -1
                        for o in range(0, count1):
                            if line[o] in '.!?':
                                st = o
                        for o in range(j + 1, len(line)):
                            if line[o] in '.!?':
                                fi = o
                                break
                        prin = line[st + 1:fi + 1]
                        prin = prin.replace('&', '')
                        print('\nНайдено предложение, в котором вычисленное вырaжение чётно:')
                        win = True
                        print(prin)
        j += 1
if not win:
    print('Предложений, в которых вычисленное выражение чётно, нет.')
s = line_to_s(line)
print('\nПреобразованный текст: \n')
for i in range(len(s)):
    print(s[i])
print()

line = s_to_line(s)
srt = None
srt_min = None
st = 0
st_min = 0
fn_min = -1
for i in range(len(line)):
    if srt == None and line[i] in '.!?':
        srt = ''
        pass
    elif srt != None and line[i] in '.!?':
        if srt_min == None:
            fn_min = i
            srt += line[i]
            srt_min = srt
        elif len(srt_min) > len(srt):
            fn_min = i
            srt_min = srt
        srt = ''
    elif line[i] not in '.!?':
        if line[i] in ' &' and srt == None:
            pass
        if line[i] in ' &' and srt == '':
            pass
        elif srt == None:
            st_min = i
            srt = line[i]
        else:
            if srt == '':
                st_min = i
            srt += line[i]
line = line[:st_min] + line[fn_min + 1:]
print('\nСамое маленькое предложение: \n')
print(srt_min.replace('&',''))
s = line_to_s(line)
print('\nПреобразованный текст: \n')
for i in range(len(s)):
    print(s[i])
print()
