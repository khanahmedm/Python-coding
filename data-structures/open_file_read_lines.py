#!/usr/bin/python3

fileName = input('Enter file name:')

fh = open(fileName)

i = 1
for line in fh:
    line2 = line.strip()
    print('line ',i, ':',end = ' ')
    print(line2)
    i += 1
