# Might have made it work
# HARD STRESS TEST

# CATCH D OR W EXCEPTIONS
# catch weekly planing to drive 0

# handle input errors
# TODO MAKE WEEKLY BREAK RIGHT SO THAT INPUT WORKS


def truck_rental_header():
    # Thinking about it now, I'll bet this won't end up being centered once it iss on something else, but scratched
    # an itch for me so I'm happy.

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
                print('Debug rent_daily_charge, classification_int): ', daily_charge)
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
                print('Debug rent_weekly_charge, classification_int): ', weekly_charge)
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
          str(current_truck_choice) + ' Truck for ' + str(number_of_days) + ' day(s). This receipt is to drive the truck '
          'for ' + str(number_of_miles) + ' miles.')


def final_weekly_roundup_no_mileage(number_of_weeks, current_weekly_charge, current_truck_choice):
    final_price = number_of_weeks * current_weekly_charge
    final_price = round(final_price, 2)
    print('Your total price for this rental is $' + str(final_price) + '. You are renting a class ' +
          str(current_truck_choice) + ' Truck for ' + str(number_of_weeks) + ' week(s), and are under the base mileage')


def final_weekly_roundup_with_mileage(number_of_weeks, current_weekly_charge, current_truck_choice, number_of_miles, current_mileage_charge):
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
            print('Debug truck_choice, classification_int: ', current_truck_choice, classification_int)
            type_choice = daily_or_weekly_choice()
            print('Debug type_choice: ', type_choice)

            if type_choice == 'D':
                number_of_days, current_daily_charge = base_rent_daily_charge(classification_int)
                print('Debug number_of_days, current_daily_charge,): ', number_of_days, current_daily_charge)
                current_mileage_charge = base_daily_mileage_charge(classification_int)
                print('Debug current_mileage_charge: ', current_mileage_charge)
                cost_for_miles, number_of_miles = number_of_miles_daily(current_mileage_charge)
                print('Debug cost_for_miles, number_of_miles: ', cost_for_miles, number_of_miles)
                final_daily_roundup(number_of_days, current_daily_charge, current_truck_choice, cost_for_miles, number_of_miles)

            elif type_choice == 'W':
                number_of_weeks, current_weekly_charge = base_rent_weekly_charge(classification_int)
                print('Debug current_weekly_charge, classification_int): ', current_weekly_charge, classification_int)
                current_mileage_charge = base_weekly_mileage_charge(classification_int)
                print('Debug current_mileage_charge: ', current_mileage_charge)
                cost_for_miles_weekly, number_of_miles = number_of_miles_weekly(current_mileage_charge)
                print('Debug cost_for_miles_weekly, number_of_miles: ', cost_for_miles_weekly, number_of_miles)
                over_200_check = check_number_of_weekly_miles(number_of_miles)
                print('Debug over_200_check: ', over_200_check)
                if over_200_check == 0:
                    final_weekly_roundup_no_mileage(number_of_weeks, current_weekly_charge, current_truck_choice)
                elif over_200_check == 1:
                    final_weekly_roundup_with_mileage(number_of_weeks, current_weekly_charge, current_truck_choice, number_of_miles, current_mileage_charge)

        elif menu_choice == 'X':
            quit()

        elif menu_choice != 'R' or 'X':
            print('Please enter either R to rent a truck or X to exit the application.')
            continue
#


main()
