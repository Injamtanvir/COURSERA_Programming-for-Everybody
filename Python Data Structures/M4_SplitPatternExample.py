fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): 
        continue
    words = line.split()
    print(words[2])


print('\n=================Another Code==============')  
print('=================Double Split Pattern==============\n')  

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '): 
        words = line.split()
        email = words[1]
        pieces = email.split('@')
        print(pieces[1]) 
    