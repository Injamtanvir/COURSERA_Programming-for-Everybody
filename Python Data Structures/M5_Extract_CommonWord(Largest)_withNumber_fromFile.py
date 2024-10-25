# Count the number of words in a file


# Sequential --> A short Python "story" about how to count words in a file
# input() --> A word used to read data from a user
name = input("Please Enter file name: ")    
try:
    handle = open(name)
except:
    print("File not found: ", name)
    quit()


# Sequential --> A short Python "story" about how to count words in a file
counts = dict()


# Repeated --> A sentence about updating one of the many counts
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


# Sequential --> A short Python "story" about how to count words in a file
bigcount = None
bigword = None


# Repeated --> A sentence about updating one of the many counts
for word, count in counts.items():


    # Conditional --> A paragraph about how to find the largest item in a list
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count


# Sequential --> A short Python "story" about how to count words in a file
print(bigword, bigcount)