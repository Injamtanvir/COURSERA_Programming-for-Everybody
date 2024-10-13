
largest = None   #Take this
smallest = None

while True:   #Continue asking the input
  num = input("Enter a number: ")
  try:
    if num == 'done':   #If num == done it will break the code and return final result
      print ("Maximum is",largest)
      print ("Minimum is",smallest)
      break

    num = int(num)   #convert num into a integer || this promopt use after the done cause if it's uses first than it will take done and convert it and go to the except command.

    if largest is None or largest < num:   #First number takes the places largest than if largest come than it will swap
      largest = num   #swapping the value

    elif smallest is None or smallest > num:    #First number takes the places smallest than if smallest come than it will swap
      smallest = num  #swapping the value

  except:
    print ("Invalid input")
