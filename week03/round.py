# round.py
# This program will read in a float and output an integer rounded up or down
# Author: Zoe McNamara Harlowe

# I got an error as the input was a string and I needed to convert it to a float

first_number = float(input("Enter a float number: "))
second_number = round(first_number)

print(first_number, "rounded is", second_number)
