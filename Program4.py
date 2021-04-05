#                                                       REMARKS
# Thomas Rose
# Programming Assignment 4
# Course: COMS-170-WWW02
# Due Feb 19 by 11:59pm
# PROGRAM DESCRIPTION
# This program assigns a random number to a variable, then takes a guess from user as to what number is. The program
# then tells the user whether their guess was higher or lower than the random number until the user guesses correctly,
# and then the user is congratulated, told how many guesses it took them, and thanked for playing.

# ______________________________________________________________________________________________________________________

#                                                      VARIABLES
#     Name         |   Type   |   Purpose
# intRandomNumber  | integer  |  This is created by assigning the result of random.randint(1, 100), which creates a
#                               'random' whole number between 1 and 100. It is for holding a secret number that the user
#                               is trying to guess, and for determining if the user has successfully guessed right

# intGuessNumber   | integer | This is created by assigning the input from 'Enter a whole number between 1 and 100,
#                              please!', and it holds at any given moment the guess that the user has entered for this
#                              iteration of the while loop. It is cleared each loop, and is used and for determining if
#                              the user has successfully guessed right

# intTries        | integer  | This is initialized before the loop starts, and acts as a counter for each time the loop
#                              has been run, IE each time the user takes a guess at the secret number. It has a value of
#                              1 added to it at the start of each loop, including the first, since even if the user
#                              guesses correctly on the first try, they will have taken one guess to win!
# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT
# _____________________________________________________________________________________________________________
#                                   Welcome to the SUPER DUPER GUESSING GAME
# -------------------------------------------------------------------------------------------------------------
# Enter a whole number between 1 and 100, please!
# >>  50
# Too High!
# Enter a whole number between 1 and 100, please!
# >>  25
# Too Low!
# Enter a whole number between 1 and 100, please!
# >>  38
# Too High!
# Enter a whole number between 1 and 100, please!
# >>  30
# Too Low!
# Enter a whole number between 1 and 100, please!
# >>  35
# Too High!
# Enter a whole number between 1 and 100, please!
# >>  33
# Congratulations, you've guessed the secret number! It only took you 6 tries, too!
# Thanks for playing!
# ______________________________________________________________________________________________________________________

# Import the random module
import random

# Sets a 'random' integer between 1 and 100 to variable 'intRandomNumber'
intRandomNumber = random.randint(1, 100)
# Initialize Variables
intTries = 0
intGuessNumber = 0
# Nice interface
print("\n_____________________________________________________________________________________________________________"
      "\n                                    Welcome to the SUPER DUPER GUESSING GAME"
      "\n-------------------------------------------------------------------------------------------------------------")
# Main Program loop
while True:
    # Add one to 'intTries' for each time the user will have taken a guess
    intTries += 1
    # Ask user for an integer between 1 and 100 and, each loop, assign it to 'intGuessNumber'
    intGuessNumber = input("Enter a whole number between 1 and 100, please!\n>>  ")
    # Convert 'intGuessNumber' to an integer
    intGuessNumber = int(intGuessNumber)

    # Determine if the user has guessed the secret number by comparing 'intGuessNumber' and 'intRandomNumber'

    # If the user has guessed correctly, congratulate them and tell them how many tries it took by
    # Displaying 'intTries' as a string. Then, end the while loop with 'quit()'
    if int(intGuessNumber) == intRandomNumber:
        print("Congratulations, you've guessed the secret number! It only took you " + str(intTries) + " tries, too!")
        print("Thanks for playing!")
        quit()

    # If the user has guessed lower than the secret number, tell them so they can make a more accurate guess, then go to
    # The next iteration of the loop via continue
    elif intGuessNumber < intRandomNumber:
        print("Too Low!")
        continue

    # If the user has guessed higher than the secret number, tell them so they can make a more accurate guess, then go
    # To the next iteration of the loop via continue
    elif intGuessNumber > intRandomNumber:
        print("Too High!")
        continue
