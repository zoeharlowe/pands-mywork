# topthree.py
# This program will generate 10 random numbers between 1 and 100
# It will then print out the top 3
# Author: Zoe McNamara Harlowe

import random

random_number = []

for i in range(10):
    random_number.append(random.randint(1,100))
print("10 random numbers: ", random_number)

random_number.sort(reverse=True)
print("Top 3: ", random_number[0:3])