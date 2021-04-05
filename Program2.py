# Thomas Rose
# Project2
# COMS-170-WWW02-W20/21
# Due: 01-22-2021
# This Program takes input from the user in the form of a retail price, then gives back a price of 20 percent off after 6 percent tax.

# Declare and initialize variables
intSalePercent = 20
intTaxPercent = 6
fltSalePrice = 0
fltTaxDollars = 0
fltFinalPrice = 0

# Get Input from the User for the Retail Price Variable
fltRetailPrice = float(input("What is the retail price of the item you would like to purchase today?\n>>> "))

# Calculate Sale Price
fltSalePrice = (fltRetailPrice * ((100 - intSalePercent) / 100))

# Calculate Amount of Tax
fltTaxDollars = (fltSalePrice * (intTaxPercent / 100))

# Calculate the Final Price
fltFinalPrice = fltSalePrice + fltTaxDollars

# Display Prices to User
print("The sale price of the item, at 20 percent off, is $" + str(fltSalePrice))
print("The tax on your purchase today, at 6 percent sales tax, is $" + str(fltTaxDollars))
print("Your total purchase price today will be $" + str(fltFinalPrice))

