# guess_random.py
# This program will prompt the user to guess a number between 1 and 100
# Author: Zoe McNamara Harlowe

import random

random_number = random.randint(1,100)

guess = int(input("Please guess a number between 1 and 100: "))
while guess != random_number:
    if guess < random_number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: "))
print ("Well done! Yes, the number was", random_number)