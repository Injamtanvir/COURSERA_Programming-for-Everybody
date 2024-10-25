name = input("Enter file: ")

if len(name) < 1:
        name = "mbox-short.txt"

try:
    handle = open(name)

except:
    print("File not found")
    quit()

file_dict={}
for line in handle :
    line=line.rstrip()
    if line.startswith("From ") :
        words=line.split()
        time=words[5]  # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
        hour_minute_split=time.split(':')
        hour=hour_minute_split[0]
        file_dict[hour]=file_dict.get(hour,0)+1

for k,v in sorted (file_dict.items()) :
    print(k,v)