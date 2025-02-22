# absolute.py
# This program will read in a number and output its absolute value
# Author: Zoe McNamara Harlowe

# I casted the input number to a float because 
# the output in the question implies we are dealing with floats

number = float(input("Enter a number: "))
absolute = abs(number)

print("The absolute value of", number, "is", absolute)