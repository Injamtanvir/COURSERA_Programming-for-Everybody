c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))

print(tmp)

print(sorted(tmp))  

tmp1 = sorted(tmp, reverse = True)  # Reverse = True this will help to reverse the sort function.
print(tmp1)

 