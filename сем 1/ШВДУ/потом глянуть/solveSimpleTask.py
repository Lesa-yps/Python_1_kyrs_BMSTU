# В файле in.txt записаны дробные числа в 8-ричной системе счисления, по одному в строке, разделитель целой и дробной части - точка.
# Требуется:
# 1. Перевести числа из исходного файла в 16-ричную систему счисления и переписать их в файл out1.txt по одному в строке в том же порядке.
# 2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.
# Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается.
# Списки, множества, словари, кортежи для сортировки не использовать.

def copy():
    tmp = open("tmp.txt", "r")
    file2 = open('out1.txt', 'w')
    while True:
        # Get next line from file
        line = tmp.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        file2.write(line)
    file2.close()
    tmp.close()
    tmp = open("tmp.txt", "w")
    tmp.write("")
    tmp.close()


file1 = open('in.txt', 'r')
count = 0
from8to2 = {
    '0': '000',
    '1': '001',
    '2': '010',
    '3': "011",
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111',
}
from2to16 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",

    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",

    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",

    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}
def mySort():
    # Сортировка
    for i in range(count):
        curmax = 0
        save = ""
        file2 = open('out1.txt', 'r')
        while True:
            # Get next line from file
            line = file2.readline()
            if (save == ""):
                save = line
            # if line is empty
            # end of file is reached
            if not line:
                break
            if len(line) > curmax:
                curmax = len(line)
                tmp = open('tmp.txt', 'a')
                tmp.write(save)
                tmp.close()
                save = line
            else:
                tmp = open('tmp.txt', 'a')
                tmp.write(line)
                tmp.close()
        with open('out2.txt', 'a') as f:
            f.write(save)
        file2.close()
        copy()
while True:
    count += 1
    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break

    part1, part2 = line.split(".")
    part1_2 = ""
    part2_2 = ""
    ans1 = ""
    ans2 = ""
    # Перевод в двоичную систему
    part1 = part1.replace("\n", '')
    part2 = part2.replace("\n", '')
    for number in part1:
        part1_2 += from8to2[number]
    for number in part2:
        part2_2 += from8to2[number]
    # приводим к правильной длине
    while len(part1_2) % 4 != 0:
        part1_2 = '0' + part1_2
    while len(part2_2) % 4 != 0:
        part2_2 = '0' + part2_2
    # Переводим обратно в 16
    for i in range(len(part1_2) // 4):
        ans1 += from2to16[part1_2[4 * i:4 * i + 4]]
    for i in range(len(part2_2) // 4):
        ans2 += from2to16[part2_2[4 * i:4 * i + 4]]
    with open('out1.txt', 'a') as f:
        f.write(ans1 + '.' + ans2 + '\n')
file1.close()
# Раскоментировать, если нужна сортировка(2 часть. Иначе out1.txt будет повреждён)
# mySort()