#!/usr/bin/python3

import re

x = 'From: Using the : character'

y = re.findall('^F.+', x)
print(y)

y = re.findall('^F.+:', x)
print(y)

y = re.findall('^F...:', x)
print(y)

y = re.findall('^F.+?:', x)
print(y)

y = re.findall('\sU.+:', x)
print(y)
