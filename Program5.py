#                                                       REMARKS
# Thomas Rose
# Programming Assignment 5
# Course: COMS-170-WWW02
# Due Mar 5 by 11:59pm
# PROGRAM DESCRIPTION
# This program uses a variety of functions to display a menu of choices regarding a Jumping Adventure Zone. One function
# starts the menu, one displays admission options, one calculates admissison costs, and one calculates a service charge.
# ______________________________________________________________________________________________________________________

#                                                      VARIABLES
#     Name                    |  Type  |   Purpose
# strMenuSelection            | string | to choose between menu selections that the user might want to pursue
# strKeyPress                 | string | waits for a keypress to move to the next menu
# strPressedKeys              | string | waits for a keypress to move to the next menu
# fltSubtotal                 | float  | holds the result from CalculateAdmission()
# fltHandling                 | float  | holds the result from CalcServiceFee(fltSubtotal)
# fltTotalCostofAdmission     | float  | holds the result of fltHandling + fltSubtotal
# intNumberVisitors           | integer| holds the input asking user for the number of visitors
# fltNumberHours              | float  | holds the input asking user for the number of hours
# fltAdmissionCost            | float  | holds return result of CalculateAdmission()
# fltServiceFee               | float  | holds return result of CalculateAdmission() CalcServiceFee(subtotal)
# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT
# Welcome to Jumpers Adventure Zone!
# Enter C to calculate your admission cost,
# Enter D to display admission options, or
# Enter X to exit the application

# >> D
# Admission Options:
# 1.0 HOURS      $14.00
# 1.5 HOURS      $17.00
# 2.0 HOURS      $20.00


# Press enter to continue...
# Welcome to Jumpers Adventure Zone!
# Enter C to calculate your admission cost,
# Enter D to display admission options, or
# Enter X to exit the application

# >> C
# How many visitors?
# > 3
# And how many hours do you want to visit us(1.0, 1.5, or 2.0)?
# > 1.5
# The cost of admission would be $55.08

# Press enter to continue...

# Welcome to Jumpers Adventure Zone!
# Enter C to calculate your admission cost,
# Enter D to display admission options, or
# Enter X to exit the application

# >> C
# How many visitors?
# > 1
# And how many hours do you want to visit us(1.0, 1.5, or 2.0)?
# > 1
# The cost of admission would be $15.12

# Press enter to continue...
# Welcome to Jumpers Adventure Zone!
# Enter C to calculate your admission cost,
# Enter D to display admission options, or
# Enter X to exit the application

# >> C
# How many visitors?
# > 12
# And how many hours do you want to visit us(1.0, 1.5, or 2.0)?
# > 2
# The cost of admission would be $259.2

# Press enter to continue...
# Welcome to Jumpers Adventure Zone!
# Enter C to calculate your admission cost,
# Enter D to display admission options, or
# Enter X to exit the application

# >> X
# Bye bye now.

# Process finished with exit code 0

# ______________________________________________________________________________________________________________________
#                                           PROGRAM


# Displays options, and runs logic for total cost of admission finding
def MainFunction():
    strMenuSelection = ''
    while True:
        print("Welcome to Jumpers Adventure Zone!"
              "\nEnter C to calculate your admission cost,"
              "\nEnter D to display admission options, or"
              "\nEnter X to exit the application")
        strMenuSelection = input('\n>> ')
        if strMenuSelection == 'C':
            strPressedKeys = ''
            while True:
                fltSubtotal = 0
                fltTotalCostofAdmission = 0
                fltHandling = 0
                fltSubtotal = CalculateAdmission()
                fltHandling = CalcServiceFee(fltSubtotal)
                fltTotalCostofAdmission = (fltHandling + fltSubtotal)
                fltTotalCostofAdmission = round(fltTotalCostofAdmission, 2)
                print("The cost of admission would be $" + str(fltTotalCostofAdmission))
                strPressedKeys = input('\nPress enter to continue... ')
                if strPressedKeys != "":
                    break
                break
        elif strMenuSelection == 'D':
            DisplayFees()
            continue
        elif strMenuSelection == 'X':
            print('Bye bye now.')
            quit()


# Displays all the fees
def DisplayFees():
    strKeyPress = ''
    while True:
        print("      Admission Options:    "
              "\n     1.0 HOURS      $14.00"
              "\n     1.5 HOURS      $17.00"
              "\n     2.0 HOURS      $20.00"
              "\nPress enter to continue...")
        strKeyPress = input('\n ')
        if strKeyPress != "":
            break
        break


# Calculates base admission cost
def CalculateAdmission():
    intNumberVisitors = 0
    fltNumberHours = 0
    fltAdmissionCost = 0.0
    intNumberVisitors = float(input("How many visitors?\n>  "))
    fltNumberHours = float(input("And how many hours do you want to visit us (1.0, 1.5, or 2.0)?\n>  "))
    if fltNumberHours == 1.0:
        fltAdmissionCost = (intNumberVisitors * 14.00)
    elif fltNumberHours == 1.5:
        fltAdmissionCost = (intNumberVisitors * 17.00)
    elif fltNumberHours == 2.0:
        fltAdmissionCost = (intNumberVisitors * 20.00)
    return fltAdmissionCost


# Calculates service fee
def CalcServiceFee(subtotal):
    fltServiceFee = 0
    fltServiceFee = (subtotal * 0.08)
    return fltServiceFee

# Call main function
MainFunction()
