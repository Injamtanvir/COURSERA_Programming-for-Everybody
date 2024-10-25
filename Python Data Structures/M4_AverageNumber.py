
# In Data Structure it takes Less Memory
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': 
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("Average:", average)


print('\n=================Another Code==============\n')  


# In Data Structure it takes More Memory
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': 
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Average:", average)