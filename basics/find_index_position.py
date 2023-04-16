#!/usr/bin/python3

text = "X-DSPAM-Confidence:    0.8475"

l = len(text)

#print(l) 

pos = text.find('  ')

#print(pos)

num = float(text[pos:].strip())

#print(num)
#print(text)
#print(text[-10:])
#print(text[-(l-pos):])

num = float(text[-(l-pos):].strip())
print(num)


