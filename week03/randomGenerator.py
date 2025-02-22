# randomGenerator.py
# This program will generate a random number between 1 and 10
# Author: Zoe McNamara Harlowe

import random

first_number = int(input("Please enter the minimum number: "))
second_number = int(input("Please enter the maximum number: "))

number = random.randrange(first_number,second_number)

print("Here is a random number: {}".format(number))
