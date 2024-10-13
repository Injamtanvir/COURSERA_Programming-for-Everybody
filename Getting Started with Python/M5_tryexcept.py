inp = input("Please enter a number: ")

try:
    ival = int(inp)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print("Not a number")
