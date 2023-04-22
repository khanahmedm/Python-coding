#!/usr/bin/python3

fh = open('mbox-short.txt')
counts = dict()

for line in fh:
    line = line.strip()
    words = line.split()
    
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)

