largest_val = -1
print('Before:', largest_val)
for num in [9, 41, 12, 3, 74, 15]:
    if num > largest_val:
        largest_val = num
    print(largest_val, num)

print('After:', largest_val)