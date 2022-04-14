# !/usr/bin/python3
import sys
import re

param1 = (sys.argv[1])
param2 = int(sys.argv[2])

data = open(param1, "rt", encoding='UTF8')
line = data.readlines()
