# InjamTanvir(INJAM UL HAQUE)

import re

# Greedy Matching
X = 'From: Using the : character'
y = re.findall('^F.+:', X)
print(y)


# Non-Greedy Matching
X = 'From: Using the : character'
y = re.findall('^F.+?:', X)  # ? is used to make it non-greedy--> one or more characters but not greedy
print(y)
