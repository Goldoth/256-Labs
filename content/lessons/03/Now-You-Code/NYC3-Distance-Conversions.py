'''
Now You Code 3: Distance Conversions

Write a Python program to enter a distnace in feet then convert that
distance to yards and miles. 

For example:

    Enter distance in FEET:15000
    That's 5000.0 yards or 2.8

NOTES:
    - Research the converion formulas on your own.
    - Format output to one decimal place

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
#5280 feet in a mile
#3 feet to a yard
# input to enter a distance
# one line to convert feet to yards
# one line to convert feet to miles
# and a good old fashioned print line to round it all out

distance = float(input("Please enter a distance in feet: ")
yards = float(distance / 3)
miles = float(distance / 5280)
print("The distance you entered is equal to %.1f yards or %.1f miles") % (yards, miles)                
