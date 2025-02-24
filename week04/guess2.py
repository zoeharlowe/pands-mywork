# guess2.py
# This program is modified from guess1.py to give hints 'too high' and 'too low'
# I did this by adding an if statement
# Author: Zoe McNamara Harlowe

number_to_guess = 39

guess = int(input("Please guess a number: "))

while guess != 39:
    if guess < 39:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: "))
print("Well done! Yes, the number was", number_to_guess)