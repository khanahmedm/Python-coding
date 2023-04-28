#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
import json

#address = input('Enter location: ')
address = 'http://py4e-data.dr-chuck.net/comments_42.json'


url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

#print(js)
#print(js['comments'])
print('User count:', len(js['comments']))

sum = 0
#print('Name', js["comments"][0]["name"])
for item in js['comments']:
    #print('Name', item['name'])
    #print('Count', item['count'])
    sum = sum + int(item['count'])

print('Sum', sum)

