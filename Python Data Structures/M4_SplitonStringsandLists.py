abc = 'with Three words'
stuff = abc.split()
print(stuff)  # ['with', 'Three', 'words']

print(len(stuff))  # 3
print(stuff[0])  # with

for w in stuff:
    print(w)  


print('\n=================Another Code==============\n')  


line = 'A lot         of Spaces'
etc = line.split()
print(etc)  # ['A', 'lot', 'of', 'Spaces']

line = 'first;second;third'
thing = line.split()
print(thing)  # ['first;second;third']
print(len(thing))   # 1

thing = line.split(';')
print(thing)  # ['first', 'second', 'third']
print(len(thing)) # 3