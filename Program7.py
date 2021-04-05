#                                                       REMARKS
# Thomas Rose
# Programming Assignment 7
# Course: COMS-170-WWW02
# Due April 2 by 11:59pm
# PROGRAM DESCRIPTION
# This program allows Miss Othmar to record scores for her classroom. She inputs each score, and each score is appended
# to a list. When the scores are done being enteres, -1 is entered, and the program finds the max value of the list (the
# high score), the min value of the list (the low score), and the total score divided by the number of scores, or the
# avg score) and displays them all. Then, each score from the list is displayed next to the line number.

# ______________________________________________________________________________________________________________________

#                                                      VARIABLES
#     Name         |   Type  |   Purpose
# scores           | list  |  This holds an empty list at first, and then each time the user enters a score, if it's not
#                             -1, we add it to the list.

# userinp          | integer| Each time the user enters a score we check to make sure that it isn't '-1', and if not,
#                             we append the score (via this variable) to the list

# accum          | float  | This holds the total of all the items in the list, found by looping through the elements of
#                           the list

# count         | integer| This variable increments once each time the second for loop iterates, and prints to the left
#                           of each score to give a nice list number

# highscore     | float| This holds the largest score in the list, found by using max() on the list

# lowscore      | float | This holds the highest score in the list, found by using min() on the list

# avg          |float|  This holds the average of all the scores on the list, found by rounding the result of all the
#                       scores (accum) divided by the number of entries on the list (len(scores)) to 2

# ______________________________________________________________________________________________________________________

#                                                   EXPECTED OUTPUT

#                                            TEST SCORE ANALYZER


# Test Score Information
#
# Enter test score, or -1 to calculate totals: 94
# Enter test score, or -1 to calculate totals: 87
# Enter test score, or -1 to calculate totals: 95
# Enter test score, or -1 to calculate totals: 62
# Enter test score, or -1 to calculate totals: 90
# Enter test score, or -1 to calculate totals: 84
# Enter test score, or -1 to calculate totals: -1
# Highest Score:           95
# Lowest Score:            62
# Average Score:           85.33
#
# Test Scores
# ____________
# 1: 94
# 2: 87
# 3: 95
# 4: 62
# 5: 90
# 6: 84
#
# Process finished with exit code 0

# ______________________________________________________________________________________________________________________

# initialize variables
scores = []
userinp = 0
count = 0
accum = 0

# title, then take user input
print('\n                                           TEST SCORE ANALYZER\n')
print('\nTest Score Information\n')
# check that input isn't -1, so we don't accidentally add it to the list
while userinp != -1:
    # check the item is an integer with try/except
    try:
        userinp = int(input('Enter test score, or -1 to calculate totals: '))
        if userinp != -1:
            scores.append(userinp)
    except:
        print('That\'s invalid!')

# loop through and add each score to the accum variable
for score in scores:
    accum = accum + score

# find highscore with max()
highscore = max(scores)

# find lowscore with min()
lowscore = min(scores)

# find avg by rounding (accum/length of scores) to 2
avg = round((accum/len(scores)), 2)

# print out the high, low, and avg score
print('Highest Score:          ', highscore)
print('Lowest Score:           ', lowscore)
print('Average Score:          ', avg)

# print out all the scores, preceded by the line number
print('\nTest Scores\n____________')
for score in scores:
    count += 1
    print(str(count) + ': ' + str(score))
