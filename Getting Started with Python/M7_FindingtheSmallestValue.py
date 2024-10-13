smallest = None
print('Before:', smallest)
for val in [9, 41, 12, 3, 74, 15]:
    if smallest is None or val < smallest:
        smallest = val
    elif val < smallest:
        smallest = val
    print(smallest, val)
print('After:', smallest)