# Thomas Rose
# Project3
# COMS-170-WWW02-W20/21
# Due: 01-29-2021
# My program takes in an age from a user, tests that it's an integer (I suppose a float would work as well, it just
# Changes it from being a string so that it can be compared to integers in the conditional executions). Based on the
# Results of that test, it either continues with the program or gives a custom error message asking for a number, not a
# String. Then, through a series of if>elif statements, the program determines the age range of the user, and suggests
# An appropriate activity in Genesee County.

# Start the try/except conditional excecution structure
try:
    # Using the input function, get an age from the user and store it in a FLOAT type variable. Integers should work
    # just as well, but on the offchance some child is young enough to count their age in fractions of years while being
    # old enough to understand the decimal translations of those values, using a float seems the simplest way to not
    # return an error
    fltAge = float(input("Enter your age for a fun experience around town: "))

    #Check that age is possible, IE older than zero. If not, kindly return an error message
    if fltAge <= 0:
        print("Hey there partner, there might be an error.")

    # If age is less than 4 and real, this block will run
    elif fltAge > 0 and fltAge < 4:
        print("Grab a seat on Thomas the Train at Huckleberry Railroad.")

    # If age is between 4 and 9 and real, this block will run
    elif fltAge >= 4 and fltAge < 9:
        print("The splash pad at Bluebell Beach is splashtastic!")

    # If age is between 9 and 16 and real, this block will run
    elif fltAge >= 9 and fltAge < 16:
        print("Toboggan Hill is packed full of winter fun!")

    # If age is equal to or older than 16 and real, this block will run
    elif fltAge >= 16:
        print("Crossroads Village is fun for adults and children.")

# If a string is entered instead of a number, give more detail so the user can succeed next time.
except:
    print("Hey there friend, please enter a numerical value next time, between 0 and 150!")
