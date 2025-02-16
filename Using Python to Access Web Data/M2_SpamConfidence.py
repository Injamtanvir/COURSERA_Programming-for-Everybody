# InjamTanvir(INJAM UL HAQUE)

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) == 1:
        num = float(stuff[0]) # stuff is a list with one element
        numlist.append(num)
print('Maximum:', max(numlist))



