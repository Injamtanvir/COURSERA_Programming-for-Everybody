# InjamTanvir(INJAM UL HAQUE)

import urllib.request, urllib.parse, urllib.error
inp = input("Enter the URL: ")
fhand = urllib.request.urlopen(inp)  # This will work as a file handle

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print("Total words in the given Url", counts) 

# http://data.pr4e.org/romeo.txt