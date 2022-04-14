# !/usr/bin/python3
import sys
import re

param1 = (sys.argv[1])
param2 = int(sys.argv[2])

data = open(param1, "rt", encoding='UTF8')
line = data.readlines()

count = {}

for str_line in line:
    words = str_line.split()

    for word in words:
        word = ''.join(filter(str.isalnum,word))
        count[word] = count.get(word,0) + 1

sort_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

cnt = 0

for key, val in sort_count.items():
    if int(sys.argv[2])==cnt:
        break
    print("{:<10}".format(key) + "{:>5}".format(val))
    cnt += 1

data.close()
