(No subject)
Chris Berkowitz

​Chris Berkowitz​
'''
Homework 6 Tip Calculator!
Christopher Berkowitz
2/18/26
Calculates the total cost of the bill including tip, as well as how much people will need to pay if they split the bill
'''

# libraries
import math

# intro line
print("\tWelcome to the Berkowitz Tip Calculator!")

# getting all the relevent numbers
billCost = float(input("What was the cost of the bill? >> "))
billSplit = int(input("How many people are splitting the bill? >> "))
tipPercent = float(input("What percent tip do you want to give? >> "))/100
taxPercent = (float(input("What percent tax was put on the bill? >> "))/100) + 1

# calculating all the numbers
billTotal = round(((billCost*taxPercent) + (billCost*tipPercent)), 2) # total price of the bill
uniqueTips = round((((billCost*taxPercent)*tipPercent)/billSplit), 2) # each person's tip cost
uniqueTotal = round((billTotal/billSplit), 2) # each person's total portion of the bill

# outputting all the numbers

# the if statements are checking if the output is a decimal or not, then converting to an int only if not
if (billTotal == math.floor(billTotal)):
    print(f"The total bill will cost ${int(billTotal)}.")
else:
    print(f"The total bill will cost ${billTotal}.")

if (uniqueTips == math.floor(uniqueTips)):
    print(f"Each person will need to tip ${int(uniqueTips)}.")
else:
    print(f"Each person will need to tip ${uniqueTips}.")

if (uniqueTotal == math.floor(uniqueTotal)):
    print(f"Each person will need to pay a total of ${int(uniqueTotal)}.")
else:
    print(f"Each person will need to pay a total of ${uniqueTotal}.")
