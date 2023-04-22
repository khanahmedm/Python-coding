#!/usr/bin/python3

import re

fh = open('mbox-short.txt')

email_list = []

for line in fh:
    line = line.rstrip()
    if re.search('^From (\S+@\S+)', line):
        #print(re.search('^From (\S+@\S+)', line))
        #x = re.findall('^From (\S+@\S+)', line)
        #print(x)
        y = re.findall('^From (\S+?@\S+)', line)
        print(y)

        email_list.append(y[0])

email_addr_list = sorted(set(email_list))

print()
print('Printing sorted email address list:')
for email in email_addr_list:
    print(email)
