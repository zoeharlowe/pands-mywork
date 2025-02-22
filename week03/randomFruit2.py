# randomFruit.py
# This program will randomly select a fruit from a list of 5 fruits
# Author: Zoe McNamara Harlowe

import random
fruit = ("apple", "banana", "raspberry", "grapes", "strawberry")

# Get a random number between 0 and length-1

index = random.randint(0,len(fruit)-1)
print("A random fruit: {}".format(fruit[index]))