x = ('Glenn', 'Sally', 'Joseph')
print(x[2])  # Joseph

y = (1, 9, 2)
print(y)  # (1, 9, 2)

print(max(y))  # 9

for iter in y:
    print(iter)


print("\n==============Another Code====================\n")

#List
x = [9, 8, 7]
x[2] = 6
print(x)  # [9, 8, 6]

y = 'ABC'
# y[2] = 'D'  # TypeError: 'str' object does not support item assignment

z = (5, 4, 3)
# z[2] = 0  # TypeError: 'tuple' object does not support item assignment



print("\n==============Another Code====================\n")

# Tuple: Not to do with tuple

x = (3, 2, 1)
# x.sort()   # AttributeError: 'tuple' object has no attribute 'sort'
# x.append(5)  # AttributeError: 'tuple' object has no attribute 'append'
# x.reverse()   # AttributeError: 'tuple' object has no attribute 'reverse'



print("\n==============Another Code====================\n")


l = list()
print(dir(l))

t = tuple()
print(dir(t))

