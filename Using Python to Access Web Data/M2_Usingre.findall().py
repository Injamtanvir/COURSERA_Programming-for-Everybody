# InjamTanvir(INJAM UL HAQUE)

# Using re.findall() method
import re
x = 'My 2 favorite numbers are 19 and 42 and Favoutite vowels are A, U'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

