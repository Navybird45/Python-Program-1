#                                                       REMARKS
# XXXXXXXXX
# Final Project - Truck Rental Modular
# XXXXXXXXX
# XXXXXXXXX
# PROGRAM DESCRIPTION
# This program calculates a truck rental rate for a customer and displays it to the screen; from the main menu, the user
# will first select a truck classification, then allow the user to decide on renting by either day or week. The user
# enters a number of days or weeks to rent the truck, then a number of miles to drive the truck for. The final price is
# displayed to the screen, and then the next user is able to use the program without restarting. If the user wished to
# close the program, they can enter X at this first menu to do so.

# ______________________________________________________________________________________________________________________

#                                                      VARIABLES
#     Name                      |    Type   |   Purpose

# truck_classification_choices  |   list    | Holds the truck classes the user is able to choose from in a list

# classification_int            |  integer  | By choosing from a list of truck classes, the user inadvertently chooses
#                                             this integer as well, and it is used to operate parallel lists and choose
#                                             the list item that aligns with the proper truck class for each future list
#                                             selection

# current_truck_choice          |  string   | Holds the truck chosen by entering a number in truck_classification_choice

# daily_or_weekly               |  string   | Holds the letter entered to designate either 'D' for day or 'W' for week
#                                             in the branching section of the program

# base_daily_charge             |   list    | Holds the daily charges that can be selected from and align to truck
#                                             classification

# number_of_days                |  integer  | Holds the number of days the user will rent the truck for

# daily_charge                  |   float   | Holds the currently selected daily charge, chosen based on previously
#                                             selected truck class, and selected from the list using the
#                                             classification_int as an index

# base_charge_weekly            |   list    | Holds the weekly charges that can be selected from and align to truck
#                                             classification

# number_of_weeks               |  integer  | Holds the number of weeks the user will rent the truck for

# weekly_charge                 |   float   | Holds the currently selected weekly charge, chosen based on previously
#                                             selected truck class, and selected from the list using the
#                                             classification_int as an index

# mileage_charge_daily_rental   |   list    | Holds the daily rental costs that can be selected from and align to truck
#                                             classification

# mileage_charge                |   float   | Holds the currently selected mileage charge, chosen based on previously
#                                             selected truck class, and selected from the list using the
#                                             classification_int as an index. This is used for both daily and weekly
#                                             rentals

# mileage_charge_weekly_rental  |   list    | Holds the weekly rental costs that can be selected from and align to truck
#                                             classification

# number_of_miles               |  integer  | Holds the number of miles the user will drive the truck for. This is used
#                                             for both daily and weekly rentals

# daily_mileage_charge          |   float   | Holds the result of current_mileage_charge * number_of_miles, which is the
#                                             currently selected daily mileage charge chosen by truck class multiplied
#                                             with the number of miles to be driven

# weekly_mileage_charge         |   float   | Holds the result of current_mileage_charge * number_of_miles, which is the
#                                             currently selected weekly mileage charge chosen by truck class multiplied
#                                             with the number of miles to be driven. This is actually unused for all
#                                             intents and purposes in the final version of the program, since we first
#                                             compare the mileage driven to 200 to check how to proceed with weekly
#                                             rentals

# current_daily_charge          |   float   | Holds return that equals daily_charge

# cost_for_miles                |   float   | Holds return that equals daily_mileage_charge

# final_daily_price             |   float   | Holds the final price of the rental, rounded to 2 places, when renting by
#                                             the day. Found with expression ((number_of_days * current_daily_charge) +
#                                             (cost_for_miles))

# current_weekly_charge         |   float   | Holds return that equals weekly_charge

# current_mileage_charge        |   float   | Holds return that equals mileage_charge

# miles_past_200                |  integer  | Holds the number of miles past 200 that the user will be driving, found
#                                             with expression (number_of_miles - 200)

# final_price                   |   float   | Holds the final price of the rental, rounded to 2 places, when renting by
#                                             the week. Used for both weekly rental situations, both with and without
#                                             mileage

# menu_choice                   |  string   | Holds the current menu choice the user wishes to make, either 'R' to rent
#                                             or 'X' to exit

# type_choice                   |  string   | Holds return that equals daily_or_weekly

# over_200_check                |  integer  | Holds value of either 1 or 0 to represent whether the current mileage is
#                                             more than 200 or not. 1 is over 200, 0 is equal to or less than 200

# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT (Top Copy)

# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > r
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > 5
# Please choose a whole number between 1 and 3
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > q
# Please choose a whole number between 1 and 3
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > 1
# You have chosen truck class A
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > q
# Enter D or W for Day or Week
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > 1
# Enter D or W for Day or Week
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > d
# You have chosen to rent by day.
# How many days do you want to rent the truck for? Enter a whole number
# > y
# Please enter a whole number equal to or greater than one
# How many days do you want to rent the truck for? Enter a whole number
# > 0
# Please enter a whole number equal to or greater than one
# How many days do you want to rent the truck for? Enter a whole number
# > 1
# How many miles are you planning to drive?
# > k
# Please enter a whole number greater than or equal to 0
# How many miles are you planning to drive?
# > 100
# Your total price for this rental is $66.95. You are renting a class A Truck for 1 day(s). This receipt is to drive
# the truck for 100 miles.
# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > q
# Please enter either R to rent a truck or X to exit the application.
# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > r
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > 2
# You have chosen truck class B
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > w
# You have chosen to rent by the week
# How many weeks do you want to rent the truck for? Enter 1 or more!
# > 1
# How many miles are you planning to drive?
# > 2000
# Your total price for this rental is $1408.59. You are renting a class B Truck for 1 week(s), and are under the base
# mileage
# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > x
#
# Process finished with exit code 0
# ______________________________________________________________________________________________________________________

def truck_rental_header():
    # Thinking about it now, I'll bet this won't end up being centered once it is on another interpreter, but looks nice
    # to me so I'm happy.
    print('-' * 50)
    print('|                TRUCK RENTAL APP                |')
    print('-' * 50)


def truck_classification_choice():
    truck_classification_choices = ['A', 'B', 'C']
    while True:
        try:
            classification_int = ((int(input('Choose a truck classification to rent from \n1) A \n2) B \n3) C'
                                             '\nEnter corresponding number\n> '))) - 1)
            if classification_int in range(3):
                current_truck_choice = truck_classification_choices[classification_int]
                print('You have chosen truck class', current_truck_choice)
                return current_truck_choice, classification_int
        except:
            pass

        print('Please choose a whole number between 1 and 3')


def daily_or_weekly_choice():
    while True:
        try:
            daily_or_weekly = input('Do you want to rent by the D day or the W week? Enter '
                                    'corresponding letter\n> ').upper()
            if daily_or_weekly == 'D':
                print('You have chosen to rent by day.')
                return daily_or_weekly
            elif daily_or_weekly == 'W':
                print('You have chosen to rent by the week')
                return daily_or_weekly

        except:
            pass

        print('Enter D or W for Day or Week')


def base_rent_daily_charge(classification_int):
    # accept classification int to find item on base_daily_charge list, return number of days and daily charge

    base_daily_charge = [17.95, 27.95, 37.95]
    while True:
        try:
            number_of_days = int(input('How many days do you want to rent the truck for? Enter a '
                                       'whole number\n> '))
            if type(number_of_days) == int and number_of_days >= 1:
                daily_charge = base_daily_charge[classification_int]
                # print('Debug rent_daily_charge, classification_int): ', daily_charge)
                return number_of_days, daily_charge

        except:
            pass

        print('Please enter a whole number equal to or greater than one')


def base_rent_weekly_charge(classification_int):
    base_charge_weekly = [107.79, 166.59, 237.99]
    while True:
        try:
            number_of_weeks = int(input('How many weeks do you want to rent the truck for? Enter '
                                        '1 or more!\n> '))
            if type(number_of_weeks) == int and number_of_weeks >= 1:
                weekly_charge = base_charge_weekly[classification_int]
                # print('Debug rent_weekly_charge, classification_int): ', weekly_charge)
                return number_of_weeks, weekly_charge

        except:
            pass

        print('Please enter a whole number equal to or greater than one')


def base_daily_mileage_charge(classification_int):
    mileage_charge_daily_rental = [0.49, 0.69, 0.79]
    mileage_charge = mileage_charge_daily_rental[classification_int]
    return mileage_charge


def base_weekly_mileage_charge(classification_int):
    mileage_charge_weekly_rental = [0.49, 0.69, 0.79]
    mileage_charge = mileage_charge_weekly_rental[classification_int]
    return mileage_charge


def number_of_miles_daily(current_mileage_charge):
    while True:
        try:
            number_of_miles = int(input('How many miles are you planning to drive?'
                                        '\n> '))
            if type(number_of_miles) == int and number_of_miles >= 0:
                daily_mileage_charge = current_mileage_charge * number_of_miles
                return daily_mileage_charge, number_of_miles

        except:
            pass

        print('Please enter a whole number greater than or equal to 0')


def number_of_miles_weekly(current_mileage_charge):
    while True:
        try:
            number_of_miles = int(input('How many miles are you planning to drive?\n> '))
            if type(number_of_miles) == int and number_of_miles >= 1:
                weekly_mileage_charge = current_mileage_charge * number_of_miles
                return weekly_mileage_charge, number_of_miles

        except:
            pass

        print('Please enter a whole number greater than or equal to 1')


def check_number_of_weekly_miles(number_of_miles):
    if number_of_miles > 200:
        return 1
    elif number_of_miles <= 200:
        return 0


def final_daily_roundup(number_of_days, current_daily_charge, current_truck_choice, cost_for_miles, number_of_miles):
    final_daily_price = ((number_of_days * current_daily_charge) + (cost_for_miles))
    final_daily_price = round(final_daily_price, 2)
    print('Your total price for this rental is $' + str(final_daily_price) + '. You are renting a class ' +
          str(current_truck_choice) + ' Truck for ' + str(number_of_days) + ' day(s). This receipt is to drive the '
          'truck for ' + str(number_of_miles) + ' miles.')


def final_weekly_roundup_no_mileage(number_of_weeks, current_weekly_charge, current_truck_choice):
    final_price = number_of_weeks * current_weekly_charge
    final_price = round(final_price, 2)
    print('Your total price for this rental is $' + str(final_price) + '. You are renting a class ' +
          str(current_truck_choice) + ' Truck for ' + str(number_of_weeks) + ' week(s), and are under the base mileage')


def final_weekly_roundup_with_mileage(number_of_weeks, current_weekly_charge, current_truck_choice, number_of_miles,
                                      current_mileage_charge):
    miles_past_200 = (number_of_miles - 200)
    final_price = ((number_of_weeks * current_weekly_charge) + (current_mileage_charge * miles_past_200))
    final_price = round(final_price, 2)
    print('Your total price for this rental is $' + str(final_price) + '. You are renting a class ' +
          str(current_truck_choice) + ' Truck for ' + str(number_of_weeks) + ' week(s), and are under the base mileage')


def main():
    menu_choice = ''
    while menu_choice != 'X':

        truck_rental_header()

        menu_choice = str(input('Type R to Rent a Truck or X to Exit\n> ')).upper()

        if menu_choice == 'R':
            current_truck_choice, classification_int = truck_classification_choice()
            # print('Debug truck_choice, classification_int: ', current_truck_choice, classification_int)
            type_choice = daily_or_weekly_choice()
            # print('Debug type_choice: ', type_choice)

            if type_choice == 'D':
                number_of_days, current_daily_charge = base_rent_daily_charge(classification_int)
                # print('Debug number_of_days, current_daily_charge,): ', number_of_days, current_daily_charge)
                current_mileage_charge = base_daily_mileage_charge(classification_int)
                # print('Debug current_mileage_charge: ', current_mileage_charge)
                cost_for_miles, number_of_miles = number_of_miles_daily(current_mileage_charge)
                # print('Debug cost_for_miles, number_of_miles: ', cost_for_miles, number_of_miles)
                final_daily_roundup(number_of_days, current_daily_charge, current_truck_choice, cost_for_miles,
                                    number_of_miles)

            elif type_choice == 'W':
                number_of_weeks, current_weekly_charge = base_rent_weekly_charge(classification_int)
                # print('Debug current_weekly_charge, classification_int): ', current_weekly_charge, classification_int)
                current_mileage_charge = base_weekly_mileage_charge(classification_int)
                # print('Debug current_mileage_charge: ', current_mileage_charge)
                cost_for_miles_weekly, number_of_miles = number_of_miles_weekly(current_mileage_charge)
                # print('Debug cost_for_miles_weekly, number_of_miles: ', cost_for_miles_weekly, number_of_miles)
                over_200_check = check_number_of_weekly_miles(number_of_miles)
                # print('Debug over_200_check: ', over_200_check)
                if over_200_check == 0:
                    final_weekly_roundup_no_mileage(number_of_weeks, current_weekly_charge, current_truck_choice)
                elif over_200_check == 1:
                    final_weekly_roundup_with_mileage(number_of_weeks, current_weekly_charge, current_truck_choice,
                                                      number_of_miles, current_mileage_charge)

        elif menu_choice == 'X':
            quit()

        elif menu_choice != 'R' or 'X':
            print('Please enter either R to rent a truck or X to exit the application.')
            continue
#


main()

# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT (Bottom Copy)

# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > r
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > 5
# Please choose a whole number between 1 and 3
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > q
# Please choose a whole number between 1 and 3
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > 1
# You have chosen truck class A
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > q
# Enter D or W for Day or Week
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > 1
# Enter D or W for Day or Week
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > d
# You have chosen to rent by day.
# How many days do you want to rent the truck for? Enter a whole number
# > y
# Please enter a whole number equal to or greater than one
# How many days do you want to rent the truck for? Enter a whole number
# > 0
# Please enter a whole number equal to or greater than one
# How many days do you want to rent the truck for? Enter a whole number
# > 1
# How many miles are you planning to drive?
# > k
# Please enter a whole number greater than or equal to 0
# How many miles are you planning to drive?
# > 100
# Your total price for this rental is $66.95. You are renting a class A Truck for 1 day(s). This receipt is to drive
# the truck for 100 miles.
# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > q
# Please enter either R to rent a truck or X to exit the application.
# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > r
# Choose a truck classification to rent from
# 1) A
# 2) B
# 3) C
# Enter corresponding number
# > 2
# You have chosen truck class B
# Do you want to rent by the D day or the W week? Enter corresponding letter
# > w
# You have chosen to rent by the week
# How many weeks do you want to rent the truck for? Enter 1 or more!
# > 1
# How many miles are you planning to drive?
# > 2000
# Your total price for this rental is $1408.59. You are renting a class B Truck for 1 week(s), and are under the base
# mileage
# --------------------------------------------------
# |                TRUCK RENTAL APP                |
# --------------------------------------------------
# Type R to Rent a Truck or X to Exit
# > x
#
# Process finished with exit code 0
