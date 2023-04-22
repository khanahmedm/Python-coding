#!/usr/bin/python3

import re

x = 'My 2 favorite numbers are 19 and 42'
print('Text is: {}'.format(x))
print()

y = re.findall('[0-9]', x)

print('Printing all digits:')
print(y)

print()
print('Printing sorted list:')
print(sorted(y))

print()
print('Printing sorted and without duplicates:')
print(sorted(set(y)))

y = re.findall('[0-9]+', x)

print()
print('Printing all numbers:')
print(y)
