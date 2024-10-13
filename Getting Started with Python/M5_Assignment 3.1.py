hr = input("Please enter hours: ")
rt = input("Please enter a rate for per hour: ")
try:
    hours = float(hr)
    rate = float(rt)
except:
    print("Please enter a numeric input")
    quit()
    
if hours <= 40:
    gross_pay = hours * rate
    print(gross_pay)

else:
    gross_pay = ((40 * rate) + ((hours - 40) * 1.5 * rate))  #Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
    print(gross_pay)

