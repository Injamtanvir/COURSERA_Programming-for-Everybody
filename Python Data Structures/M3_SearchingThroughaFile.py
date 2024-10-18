"""
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
"""

# ========================================================

"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()  # Remove the \n from every lines end
    if line.startswith('From:'):
        print(line)
"""


# ========================================================

"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue  # continue skip the lines that didn't startswith From
    print(line)
"""


# ==================Using in to select lines======================================

"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
"""


# ==================Prompt for File Name======================================

"""
fname = input("Please enter the File name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', fname)
"""


# ==================Using try, except, open======================================

fname = input("Please enter the File name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', fname)