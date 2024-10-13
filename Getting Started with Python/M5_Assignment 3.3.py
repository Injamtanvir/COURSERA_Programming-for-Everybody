score = input("Please enter a Score: ")
try:  #trying to convert input result in a floating value
    x = float(score)
except:
    print("Please enter a numeric number!!")
    quit()   #That will not execute rest of the code


if 0.0 <= x <= 1.0:   #the score is between 0.0 and 1.0
    if x >= 0.9:
        print("A")
    elif x >= 0.8:
        print("B")
    elif x >= 0.7:
        print("C")
    elif x >= 0.6:
        print("D")
    else:
        print("F")


else:
    print("error!!")
    print("Please enter a score between 0.0 and 1.0 ")
    exit()

