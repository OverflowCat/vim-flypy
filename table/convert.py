# read file test.csv line by line
from codecs import open
file = open("./for安卓百度个性短语.ini", "r", "utf-16") # UTF-16 LE
lines = file.readlines()
table = {}
for line in lines:
    line = line.strip() # 换行符问题
    splitted = line.split(',')
    code = splitted[0].split('=')[0]
    word = splitted[1]
    if code not in table:
        table[code] = [word]
    else:
        table[code].append(word)
file.close()

resultfile = open("../plugin/vimim.flypy.txt", "w", "utf-8")
for key in table:
    resultfile.write(f"{key} {' '.join(table[key])}\n")
resultfile.close()