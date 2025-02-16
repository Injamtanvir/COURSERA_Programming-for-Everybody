# InjamTanvir(INJAM UL HAQUE)

import re 

inp = input("Please enter the File name(which you want to count all the numbers on the file): ")
hand = open(inp)

count = 0
sum = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)   # There a string list was create every time to store the number value on a line
    # print(x)
    for i in x:
        count = count + 1
        sum = sum + int(i)

print(f'There are {count} values with a sum={sum}')

# regex_sum_42.txt --> There are 90 values with a sum=445833
# regex_sum_1717171.txt --> There are 109 values with a sum=474216
