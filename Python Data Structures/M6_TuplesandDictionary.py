d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)   
# csev 2
# cwen 4

# The items() method in dictionaries returns a list of (Key, value) tuples
tups = d.items()
print(tups)   # dict_items([('csev', 2), ('cwen', 4)])