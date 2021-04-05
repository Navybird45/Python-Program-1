#                                                       REMARKS
# Thomas Rose
# Programming Assignment 8
# Course: COMS-170-WWW02
# Due April 9 by 11:59pm
# PROGRAM DESCRIPTION
# This program allows the user to input sentences to have capitalized. The program will split the entered lines into a
# list of lines, using '. ' as a delimiter. Then each line is stripped, and the first letter of each line is
# capitalized with upper(), then concatenated with the rest, unaltered rest of the line. Then, each list item is
# replaced with the new item, the list is rejoined into the original string with the delimiter, and the string is
# returned. The user then has the option to run the program again by entering 'Y'.

# ______________________________________________________________________________________________________________________

#                                                      VARIABLES
#     Name         |   Type  |   Purpose

# delim            | string  | Holds the delimiter value to use to find end of entered sentences.

# seconddelim      | string  | Holds the second delimiter value, used to add a period and a space when joining sentences

# index            | integer | This holds the index value, used to reassign each  new list item to the corresponding
#                               place in the list

# userinp          | string  | Each time the user runs the program, this holds the entered sentences.

# listedsentences  |   list  | A list created from string userinp that splits the sentences with delim into seperate
#                               list items

# sentence         |parameter| This is the parameter in the for loop that holds the current sentence being capitalized,
#                               then the capitalized version of the sentence, as well as assigns the new sentence to
#                               the appropriate list item (found via index)

# outputsentence   |  string  | This holds the final, transformed string of capitalized sentences, and is created with
#                               seconddelim to add a period and space between each sentence

# inp              | string  |  This holds input and is checked to see if the user wants to run the program again

# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT

# Enter sentences for modification: my name is Samantha. i go to Mott Community College.
# Your output sentence is:
# My name is Samantha. I go to Mott Community College.
# Enter 'Y' to try again...y
# Enter sentences for modification: my favorite character is Charlie Brown. he is a great sport.
# Your output sentence is:
# My favorite character is Charlie Brown. He is a great sport.
# Enter 'Y' to try again...Y
# Enter sentences for modification: programming in Python is super FUN. i can't wait to learn more.
# Your output sentence is:
# Programming in Python is super FUN. I can't wait to learn more.
# Enter 'Y' to try again...n
#
# Process finished with exit code 0


# ______________________________________________________________________________________________________________________

# make a main function to contain code
def main():
    # make a while loop so the program can be ran multiple times
    while True:
        # initialize variables
        delim = '.'
        seconddelim = '. '
        index = 0
        # get sentences from user
        userinp = str(input('Enter sentences for modification: '))
        # split input string into a list using period as a delim
        listedsentences = userinp.split(delim)
        # iterate through each list item (sentence)
        for sentence in listedsentences:
            # check if the sentence contains characters
            if len(sentence) >= 1:
                # strip sentence
                sentence = sentence.strip()
                # make sentence th result of (first character capitalized + unaltered remaining characters)
                sentence = sentence[:1].upper() + sentence[1:]
                # assign sentence to appropriate list item using index
                listedsentences[index] = sentence
                # increment index by 1
                index += 1
            else:
                # if list item is empty, skip it.
                continue

        # make a new sentence by joining the list items of listedsentences with a period and a space (seconddelim)
        outputsentence = seconddelim.join(listedsentences)
        # return modified sentences
        print('Your output sentence is: ')
        print(outputsentence)
        # check if the user wants to run the program again with 'y' or 'Y'
        inp = input('Enter \'Y\' to try again...')
        if inp.upper() == 'Y':
            continue
        else:
            quit()


# call main() function
main()
