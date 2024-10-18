fname = input("Please Enter file name: ")
try:
    fhandle = open(fname)

except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

count = 0
total = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):    #Find which line startswith "X-DSPAM-Confidence:"
        pos = line.find(":")                        #Then find the :
        float_number = float(line[pos+1:])          #Then get float value which is after :
        count = count + 1                         #Then count every similar line
        total = total + float_number              #Then add floating values in total

print(f"Average spam confidence: {total / count}")
