# convert.py
# This program will read in a float amount of money in dollars and 
# output the absolute amount in cent
# Author: Zoe McNamara Harlowe

'''
float_amount = float(input("Enter an amount of money in dollars: "))
absolute_amount = abs(float_amount)
cent_amount = absolute_amount * 100

print ("That amount in cent is", cent_amount)
'''

# I noticed that the above code output the cent amount as a float
# I used the int() function to convert the cent amount to an integer

float_amount = float(input("Enter an amount of money in dollars: "))
absolute_amount = abs(float_amount)
cent_amount = int(absolute_amount * 100)

print ("That amount in cent is", cent_amount)
