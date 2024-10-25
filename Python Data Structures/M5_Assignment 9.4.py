name = input("Please Enter file name: ")

try:
    handle = open(name)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

count = 0
hold_name = list()

for line in handle:
    if not line.startswith("From:"):
        continue
    line = line.split()
    hold_name.append(line[1])

counts = dict()
for word in hold_name:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)

