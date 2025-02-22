# sub.py
# This program will read in 2 numbers and subtract the first number from second
# Author: Zoe McNamara Harlowe

# input reads in a string so we need to convert it to an integer to do arithmetic

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
answer = first_number - second_number
print(f"{first_number} minus {second_number} is {answer}")