# is_even2.py
# This program is based off is_even.py and is_even1.py
# It reads in a number, rounds it and outputs if it is even or odd
# It uses a while loop to get the program to continue running until the user inputs a -1
# Author: Zoe McNamara Harlowe

raw_number = 0

while raw_number != -1:
    raw_number = float(input("Please enter a number (Enter -1 to quit): "))
    rounded_number = round(raw_number)
    if rounded_number % 2 == 0:
        print(f"{rounded_number} is an even number")
    elif rounded_number != -1:
        print(f"{rounded_number} is an odd number")
print("All done")
