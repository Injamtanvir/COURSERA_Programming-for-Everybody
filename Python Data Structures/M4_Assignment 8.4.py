fname = input("Enter the file name: ")
try:
    fhandle = open(fname)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

lst = list()
for line in fhandle:
    word= line.rstrip().split()
    for elem in word:
        if elem in lst:     #For each word on each line check to see if the word is already in the list and if not append it to the list.
            continue
        else :
            lst.append(elem)
lst.sort()
print(lst)
