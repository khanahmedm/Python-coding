#!/usr/bin/python3

fh = open('mbox-short.txt')
count = 0

for line in fh:
    line = line.strip()
    if line.startswith('From'):
        count += 1

print('There are', count, "lines that start with word 'From'.")

