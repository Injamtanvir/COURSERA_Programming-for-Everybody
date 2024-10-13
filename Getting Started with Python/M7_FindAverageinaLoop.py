count = 0
sum = 0
print("Before", count, sum)
for val in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + val
    print(count, sum, val)

avg = sum / count

print("After", count, sum, avg)