fname = input("Enter file name: ")

try:
    handle = open(fname)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

count = 0
for line in handle:
    if line.startswith("From:"):
        k_split = line.rstrip().split()
        try:
            print(k_split[1])
            count = count + 1               #For Question-Answer(mbox-short.txt) : There were 27 lines in the file with From as the first word.
        except:
            continue

print("There were", count, "lines in the file with From as the first word")





# # Another Approach by Dr. Chuck
# handle = open('mbox-short.txt')

# for line in handle:
#     line = line.rstrip()
#     wds = line.split()
#     #Guardian pattern
#     if len(wds) < 3 or wds[0] != 'From':
#         continue
#     print(wds[1])