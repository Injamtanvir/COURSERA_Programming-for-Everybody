fhand = open('mbox.txt')
# print(fhand)    #Large Data will take time to show in your Terminal

# Thats why used this strip() function to remove extra new line of \n at the end of every line
for line in fhand:
    print(line.strip())