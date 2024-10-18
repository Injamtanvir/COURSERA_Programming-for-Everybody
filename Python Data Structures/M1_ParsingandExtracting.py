line = 'Have a nice day'
print(line.startswith("Have"))
print(line.startswith("H"))
print(line.startswith("h"))


print("\n==============Another Code Output================\n")


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

