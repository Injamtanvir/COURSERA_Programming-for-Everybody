# InjamTanvir(INJAM UL HAQUE)

# import re
# line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)', line) # @[^ ] is used to indicate the the start of extraction starts at @ and Match Non-Blank Character, * is used to extract 0 or more characters
# print(y)


# ===================================================================


# Extracting the host name from the email address using re.findall() method

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From.*@([^ ]*)', line)  # .*@ means any character followed by @
print(y)
