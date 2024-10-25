name = input("Please Enter file name: ")

try:
    handle = open(name)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

count = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        count[w] = count.get(w, 0) + 1



bigcount = None
bigword = None
for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
