
fname = input("Please enter the file name: ")
try:
    handle = open(fname)
except:
    print("Sorry!!\nPlease re-enter file name.")
    quit()


for line in handle:     #Catches every line.
    new_line = line.rstrip().upper()  #If we didn't use rstrip() it will catches \n from the files-lines and add extra spaces on the output.
    print(new_line)                   #upper() function uses to write the letter in upper format.
    