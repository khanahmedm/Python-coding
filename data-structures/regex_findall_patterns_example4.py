#!/usr/bin/python3

import re
from statistics import mean

fh = open('mbox-short.txt')

numlist = list()

for line in fh:
    line = line.strip()
    stuff =  re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if stuff:
        num = float(stuff[0])
        numlist.append(num)

#print(numlist)
print('Maximum spam confidence found:', max(numlist))
print('Average spam confience found:', mean(numlist))        
