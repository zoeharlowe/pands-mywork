# guess1.py
# This program will prompt the user to guess a number between 1 and 100
# It will continue until the user guesses the correct number
# Author: Zoe McNamara Harlowe

number_to_guess = 39

guess = int(input("Please guess a number: "))

while guess != 39:
    print("Wrong!")
    guess = int(input("Please guess again: "))
print("Well done! Yes, the number was", number_to_guess)
