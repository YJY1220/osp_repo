# !/usr/bin/python3
import sys
import re

param1 = (sys.argv[1])
param2 = int(sys.argv[2])

data = open(param1, "rt", encoding='UTF8')
line = data.readlines()

count = {}

from str_line in line:
    words = str_line.split()

    for word in words:
        word = ''.join(filter(str.isalnum,word))
        count[word] = count.get(word,0) + 1
