# InjamTanvir(INJAM UL HAQUE)


# Extracting email address from a line using re.findall() method

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y =  re.findall('\S+@\S+', x)  # \S+ means one or more non-whitespace characters follow by @ and then one or more non-whitespace characters
print(y)

y = re.findall('^From (\S+@\S+)', x)  # ^From means the line should start with From and then one or more non-whitespace characters follow by @ and then one or more non-whitespace characters
print(y)




# =======================================================================================================================
# Extracting the host name from the email address using find and string slicing

# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = x.find('@')
# print(atpos)

# sppos = x.find(' ', atpos)  # find the space after the @
# print(sppos)

# host = x[atpos+1 : sppos]  # from the character after @ to the character before the space
# print(host)



# =======================================================================================================================
# Extracting the host name from the email address using Double split pattern

# X = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# words = X.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])
