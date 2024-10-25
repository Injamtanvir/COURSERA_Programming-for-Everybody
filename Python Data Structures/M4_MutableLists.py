# Strings are Immutable
# Lists are Mutable
# Tuples are Immutable
# Sets are Mutable
# Dictionaries are Mutable


fruit = 'Banana'
# fruit[0] = 'b'   # Will show an Error! 
# print(fruit)  # Will show an Error!

x = fruit.lower()
print(x)  # banana

lotto = [2, 14, 26, 41, 63]
print(lotto)  # [2, 14, 26, 41, 63]

lotto[2] = 28
print(lotto)   # [2, 14, 28, 41, 63]
