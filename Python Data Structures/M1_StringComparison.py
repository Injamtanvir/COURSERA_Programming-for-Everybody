word = 'coconut' # 'coconut', 'banana', 'apple'

if word == 'banana':
    print('Yes, we have a match!') 
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print("All right, bananas.")

"""
This is actually comapare strings first value using ASCII table values. Like in ASCII Table a comes first then b, c, d and so on. So, if you compare 'banana' with 'coconut', 'banana' comes first in ASCII table. So, the output will be:
if frirst word a and a similar then it will comapare second word and so on. If all words are similar then it will print same. """