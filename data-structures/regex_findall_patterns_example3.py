#!/usr/bin/python3

import re

fh = open('mbox-short.txt')

domain_list = []

for line in fh:
    line = line.rstrip()
    if re.search('^From (\S+@\S+)', line):
        #print(re.search('^From (\S+@\S+)', line))
        #x = re.findall('^From (\S+@\S+)', line)
        #print(x)
        y = re.findall('@(\S+)', line)
        print(y)

        domain_list.append(y[0])

domain_addr_list = sorted(set(domain_list))

print()
print('Printing sorted domain address list:')
for domain in domain_addr_list:
    print(domain)
