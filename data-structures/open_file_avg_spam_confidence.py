#!/usr/bin/python3

fname = input('Enter file name:')
fh = open(fname)

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(' ')
    num = float(line[pos:].strip())
    count = count + 1
    total = total + num

avg_spam_conf = total/num

print('Average spam confidence:', avg_spam_conf)
