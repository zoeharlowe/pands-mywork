# is_even.py
# This program will read in an integer and output whether it is even or odd
# Author: Zoe McNamara Harlowe

# I casted the input number to an integer and ensured the prompt asked 
# only for integers

raw_number = int(input("Please enter an integer: "))

# Then I used an if statement to check if the number was divisible by 2
# If it was, I printed that the number was even
# If it wasn't, I used an else statement to print that the number was odd

if raw_number % 2 == 0:
    print(f"{raw_number} is an even number")
else:
    print(f"{raw_number} is an odd number")
