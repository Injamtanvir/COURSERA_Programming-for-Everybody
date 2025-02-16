# InjamTanvir(INJAM UL HAQUE)

# Using find() method

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)


# =====================================================


# Using re.search() method LIKE find() method

# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

# =====================================================

# Using startswith() method

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# =====================================================

# Using re.search() method LIKE startswith() method

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)