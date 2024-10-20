file = open('file.txt', 'w')
f2 = open('file2.txt', 'r')
ch2 = f2.readline().strip()
with open('file1.txt', 'r') as f1:
    for ch1 in f1:
        if ch2 != '' and ch1 != '':
          while int(ch1.strip()) >= int(ch2):
              file.write(ch2)
              file.write("\n")
              ch2 = f2.readline().strip()
              if ch2 != '':
                  break
        file.write(ch1)
for ch2 in f2:
    file.write(ch2)
file.close()
f2.close()
