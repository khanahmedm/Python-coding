#!/usr/bin/python3

fh = open('mbox-short.txt')
counts = dict()

for line in fh:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        word = words[5]
        hours = word.split(':')
        hour = hours[0]
        
        counts[hour] = counts.get(hour, 0) + 1

print('Sorted by keys')
for key, val in sorted(counts.items()):
    print(key, val)

#counts = sorted(counts.items, key = lambda x : x[1])
print()

print('Sorted by values')
for key, val in sorted(counts.items(), key = lambda x : x[1]):
    print(key, val)
