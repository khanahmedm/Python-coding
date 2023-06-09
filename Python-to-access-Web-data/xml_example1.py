#!/usr/bin/env python3

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('phone').get('type'))
print('Email:', tree.find('email').text)
print('Email attr:', tree.find('email').get('hide'))
print('Phone:', tree.find('phone').text)
