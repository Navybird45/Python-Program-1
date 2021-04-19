# Might have made it work
# HARD STRESS TEST

# CATCH D OR W EXCEPTIONS
# catch weekly planing to drive 0

# handle input errors
# TODO MAKE WEEKLY BREAK RIGHT SO THAT INPUT WORKS


def main():

    truck_classification_choices = ['A', 'B', 'C']
    base_daily_charge = [17.95, 27.95, 37.95]
    mileage_charge_daily_rental = [0.49, 0.69, 0.79]
    base_charge_weekly = [107.79, 166.59, 237.99]
    mileage_charge_weekly_rentals = [0.49, 0.69, 0.79]
    menu_choice = ''
    while menu_choice != 'X':

        print('-' * 50)
        print('|                TRUCK RENTAL APP                |')
        print('-' * 50)
        menu_choice = input('Type R to Rent a Truck or X to Exit\n> ').upper()

        if menu_choice == 'R':

            while True:
                try:
                    classification_int = ((int(input('Choose a truck classification to rent from \n1) A \n2) B \n3) C'
                                                     '\nEnter corresponding number\n> '))) - 1)
                    if classification_int in range(4):
                        current_truck_choice = truck_classification_choices[classification_int]
                        print('You have chosen truck class', current_truck_choice)
                        break
                except:
                    pass

                print('Please choose an integer between 1 and 3')

            # def files(a):
            #     pass
            #
            # while True:
            #     try:
            #         i = int(input('Select: '))
            #         if i in range(4):
            #             files(i)
            #             break
            #     except:
            #         pass
            #
            #     print
            #     '\nIncorrect input, try again'

            while True:
                try:
                    daily_or_weekly = input('Do you want to rent by the D day or the W week? Enter '
                                            'corresponding letter\n> ').upper()
                    if daily_or_weekly == 'D':
                        print('You have chosen to rent by day.')
                        while True:
                            try:
                                number_of_days = int(input('How many days do you want to rent the truck for? Enter a '
                                                           'whole number\n> '))
                                if type(number_of_days) == int:
                                    current_daily_charge = base_daily_charge[classification_int]
                                    while True:
                                        try:
                                            number_of_miles = int(input('How many miles are you planning to drive?'
                                                                        '\n> '))
                                            if type(number_of_miles) == int:
                                                mileage_charge = mileage_charge_daily_rental[classification_int]
                                                final_daily_price = ((number_of_days * current_daily_charge) +
                                                                     (mileage_charge * number_of_miles))
                                                final_daily_price = round(final_daily_price, 2)
                                                print('Your total price for this rental is $' + str(final_daily_price) +
                                                '. You are renting a class ' + current_truck_choice + ' Truck for ' +
                                                str(number_of_days) + ' day(s). This receipt is to drive the truck for '
                                                + str(number_of_miles) + ' miles.'
                                                    )
                                                break
                                        except:
                                            pass

                                        print('Please enter an integer')

                                    break
                                break
                            except:
                                pass
                            print('Please enter an integer')
                        break

                    elif daily_or_weekly == 'W':
                        print('You have chosen to rent by week.')
                        while True:
                            try:
                                number_of_weeks = int(input('How many weeks do you want to rent the truck for? Enter '
                                                            '1 or more!\n> '))
                                if number_of_weeks >= 1:
                                    current_weekly_charge = base_charge_weekly[classification_int]
                                    while True:
                                        try:
                                            number_of_miles = int(input('How many miles are you planning to drive?'
                                                                        '\n> '))
                                            if number_of_miles > 0:
                                                mileage_charge = mileage_charge_weekly_rentals[classification_int]
                                                cost_before_mileage = number_of_weeks * current_weekly_charge

                                                if number_of_miles > 200:
                                                    final_weekly_price = (cost_before_mileage + ((number_of_miles - 200)
                                                                                                 * mileage_charge))
                                                    print(final_weekly_price)
                                                    break

                                                else:
                                                    final_weekly_price = cost_before_mileage
                                                    print(final_weekly_price)
                                                    break

                                            break

                                        except:
                                            pass

                                        print('Enter a whole number of miles greater than 0')
                                break

                            except:
                                pass

                            print('Enter a whole number of weeks 1 or greater')

                    break


                except:
                    pass

                print('Enter D or W for Day or Week')

        elif menu_choice == 'X':
            quit()

        else:
            print('Please enter either R to rent a truck or X to exit the application.')
            continue


main()
