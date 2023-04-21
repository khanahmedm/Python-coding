#!/usr/bin/python3

fh = open('romeo.txt')
s = list()

for line in fh:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in s:
            s.append(word)

s.sort()
print(s)
