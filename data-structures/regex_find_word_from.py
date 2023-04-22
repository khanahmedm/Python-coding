#!/usr/bin/python3

import re

filename = 'mbox-short.txt'
fh = open(filename)
count = 0

for line in fh:
    line = line.strip()
    if re.search('From:', line):
        print(line)
        count += 1

print('There are', count, "occurences of the word 'From:' in the file", filename, '.')
print()
print('Printing with format()')
print("There are {} occurences of the word 'From:' in the file {}.".format(count, filename))
