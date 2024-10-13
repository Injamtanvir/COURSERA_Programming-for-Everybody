def computepay(h, r):    #function called computepay()
    if h <= 40:
        gross_pay = h * r
        return gross_pay
    else:
        gross_pay = ((40 * r) + ((h - 40) * 1.5 * r)) #Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
        return gross_pay


hours = input("Please enter hours: ")
rate = input("Please enter a rate for per hour: ")

try:    #for converting string to float
    h = float(hours)
    r = float(rate)
except:
    print("Sorry!!")
    print("Please enter a Numeric value!!")
    quit()

p = computepay(h, r)  #called function and passes h & r as a parameter
print("Pay", p)

