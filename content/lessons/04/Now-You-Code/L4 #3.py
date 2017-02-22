##TODO
##allow for point value input
##if else and elif statements to determine grade
##try and except statements to handle bad input
##points should be entered as integers

try:
    print("IST 256 Grade Calculator")
    points = int(input("Please enter your total points out of 600 for the course: "))
    if points <= 299:
            print(("With a total of %d points your grade in the class is an: F") % (points))
            ## using %d in line to call points for a correct value
    elif 300 <= points <= 359:
            print(("With a total of %d points your grade in the class is a: D") % (points))
            ##creating a range with <= to allow all point values within the range to return an answer
    elif 360 <= points <= 389:
            print(("With a total of %d points your grade in the class is a: C-") % (points))
    elif 390 <= points <= 419:
            print(("With a total of %d points your grade in the class is a: C") % (points))
    elif 420 <= points <= 449:
            print(("With a total of %d points your grade in the class is a: C+") % (points))
    elif 450 <= points <= 479:
            print(("With a total of %d points your grade in the class is a: B-") % (points))
    elif 480 <= points <= 509:
            print(("With a total of %d points your grade in the class is a: B") % (points))
    elif 510 <= points <= 539:
            print(("With a total of %d points your grade in the class is a: B+") % (points))
    elif 540 <= points <= 569:
            print(("With a total of %d points your grade in the class is a: A-") % (points))
    elif 570 <= points <= 600:
            print(("With a total of %d points your grade in the class is a: A") % (points))
    else:
            print("Please enter a valid point total between 0 and 600")
except ValueError:
        print("That is not a valid score, please enter an integer value between 0 and 600")

##the try and except statements handle inputs other than integers for the variable points
