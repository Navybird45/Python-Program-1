#                                                       REMARKS
# Thomas Rose
# Programming Assignment 6
# Course: COMS-170-WWW02
# Due Mar 26 by 11:59pm
# PROGRAM DESCRIPTION
# This program reads a file from a hardcoded file containing a list of sales data. The program allows the user to choose
# from three options: Display Sales, which reads the file and prints to screen a display of that data, but with a
# counter - based line number to the left of each line; Calculate Totals, which reads the file, converts each line to a
# float, adds a running total of all the sales items to an accumulator value, finds the average by dividing the
# accumulator value by a counter value, and then returns both values back to the main function; and Exit Application,
# which exits the application.

# ______________________________________________________________________________________________________________________

#                                                      VARIABLES
#     Name         |   Type  |   Purpose
# strmenuselection | string  |  This holds an empty string at first so 'while strmenuselection != 'X'' has something to
#                                check. Then it holds the input from the user for menu selection. Due to .upper() it can
#                                be a lowercase form of the menu selection letters.

# fltgrandtotal    | float/   | This holds the first return value from CalcTotal() and represents the total of all the
#                    string           sales in the file, rounded to 2 decimal places.

# fltavgsaleamount | float/  | This holds the second return value from CalcTotal() and represents the average of all the
#                    string           sales in the file, rounded to 2 decimal places.

# count            | integer| This variable appears locally twice, but is initialized each time so we can use it without
#                             fear. When reading the file, it increments each time a line is read through to provide a
#                             running total of the lines in the file, and concurrently represents the number of sales
#                             logged in the file.

# accum            | float| This holds the total of all the sales logged in the file by adding the sale value to the
#                             variable total each time a line in the file is read. After being rounded to 2 decimal
#                             places, it is returned from CalcTotal() and unpacked to fltgrandtotal.

# avg             | float | The result of accum/count is saved to this variable, which represents the average of all the
#                           sales in the file. After being rounded to 2 decimal places, it is returned from CalcTotal()
#                           and unpacked to fltavgsaleamount.

# line      |string/float|  This variable appears locally twice, both times to hold the .strip() version of the line
#                           currently being parsed in the file. The second time, it also stores a float version of the
#                           line currently being parsed.

# line2           |string|  This variable holds a new string that concatenates the count variable and the line currently
#                           being parsed from the file in order to make a new line that has a line counter to the left
#                           of each line, which is then printed to the screen in DisplaySales()

# keypress      | string | waits for a keypress to go back to main menu

# pressedkey    | string | waits for a keypress to go back to main menu
# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT
# POPCORN SALES
#
# D: Display Sales
# C: Calculate Total and Average
# X: Exit Application
#
# Enter your menu selection:  P is for Popcorn
# Try that again!
#
# POPCORN SALES
#
# D: Display Sales
# C: Calculate Total and Average
# X: Exit Application
#
# Enter your menu selection:  d
# POPCORN SALES
# 1: $50
# 2: $17.32
# 3: $32.99
# 4: $51.02
# 5: $15.61
# 6: $23.94
# 7: $5.99
# 8: $12.1
# 9: $62.74
# 10: $105.59
# 11: $16.50
# 12: $32.99
# 13: $23.71
# 14: $54.90
# 15: $19
# 16: $17.52
# 17: $48.6
# 18: $102
# 19: $99.99
# 20: $73.05
# Press enter to continue...
#
# POPCORN SALES
#
# D: Display Sales
# C: Calculate Total and Average
# X: Exit Application
#
# Enter your menu selection:  C
# The grand total was $865.56
# The average sale amount was $43.28
#
# Press enter to continue... x
#
# POPCORN SALES
#
# D: Display Sales
# C: Calculate Total and Average
# X: Exit Application
#
# Enter your menu selection:  x
#
# Process finished with exit code 0
# ______________________________________________________________________________________________________________________



# the menu structure that powers the program
def main():
    # Give first while loop something to compare to
    strmenuselection = ''
    # If input is x, make false so the program can quit
    while strmenuselection != 'X':
        print('\nPOPCORN SALES\n')
        print(
            'D: Display Sales\n'
            'C: Calculate Total and Average\n'
            'X: Exit Application\n'
              )
        # I actually did the research and I don't need the str() here since input makes a string, but it's a safeguard
        # So removing it makes me wary even if it's not needed now.
        strmenuselection = str(input('Enter your menu selection:  '))
        # Make input play nice so lowercase characters can be input for the same effect as uppercase
        strmenuselection = strmenuselection.upper()
        if strmenuselection == 'D':
            # This calls DisplaySales()
            DisplaySales()

        elif strmenuselection == 'C':
            # This calls CalcTotal(), but also does most of the formatting for the return info and displays it nicely
            while True:
                # This structure allows the 'Press enter to continue... ' to function
                fltgrandtotal, fltavgsaleamount = CalcTotal()
                fltgrandtotal = str(fltgrandtotal)
                fltavgsaleamount = str(fltavgsaleamount)
                print('The grand total was $' + fltgrandtotal)
                print('The average sale amount was $' + fltavgsaleamount)
                keypress = input('\nPress enter to continue... ')
                # Once input is filled and the enter key is hit, the program breaks back to the main menu
                if keypress != '':
                    break
                break
        # Stops the 'Try that again' message from displaying when exiting program
        elif strmenuselection != 'X':
            print('Try that again!')
            continue


# A function that reads through each line of the file, using a counter to create new lines with line number added to the
# left of each line, as well as formatting for dollars
def DisplaySales():
    # This structure allows the 'Press enter to continue... ' to function
    while True:
        count = 0
        # Handle incorrect, hardcoded filenames, quit code if file not found
        try:
            fhand = open('saledata.txt', 'r')
        except:
            print('The file couldn\'t be opened!')
            quit()
        print('POPCORN SALES')
        for line in fhand:
            count += 1
            line = line.strip()
            line2 = str(count) + ': $' + line
            print(line2)
        pressedkey = input('Press enter to continue...')
        # Once input is filled and the enter key is hit, the program breaks back to the main menu
        if pressedkey != '':
            break
        break

# This function turns each line in the file into a float, adds it to an accumulator variable, then returns the total
# of all the sales (accumululator rounded to 2 decimal places), as well as the average sale amount (accumulator divided
# by the total number of sales, tracked with a counter variable
def CalcTotal():
    accum = 0
    count = 0
    # Handle incorrect, hardcoded filenames, quit code if file not found
    try:
        fhand = open('saledata.txt', 'r')
    except:
        print('The file couldn\'t be opened!')
        quit()
    for line in fhand:
        count += 1
        line = line.strip()
        line = float(line)
        accum = accum + line
    accum = round(accum, 2)
    avg = (accum / count)
    avg = round(avg, 2)
    return accum, avg

# Run the program by calling main()
main()
