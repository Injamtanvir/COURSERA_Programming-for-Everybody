fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))  # We can read the whole file(newline and all) into a single string

print(inp[:20]) #Prints the first 20 characters of the file