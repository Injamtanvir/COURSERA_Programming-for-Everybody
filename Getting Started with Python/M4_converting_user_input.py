# Convert Elevator Floors to USA Style

# --> In European Method Building Floor Starts with Groumd(0), But in USA Building floor starts with 1
inp = input("Please type European Floor Number: ")
usf = int(inp) + 1
print("US floor", usf)