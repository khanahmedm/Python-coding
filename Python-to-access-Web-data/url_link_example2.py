#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
numlist = list()
#tags = soup('span')
tags = soup('td')
print(tags)
line_num = 1

for tag in tags:
    line_num += 1
    name = str(tag.contents[0])

    if not name.find('span') > 0:
        if name not in ['Comments', 'Name']:
            print('line number:', line_num, ' - ', tag.contents[0])

