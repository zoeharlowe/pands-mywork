# count_function.py
# This program contains a function which will read in the contents of another file (count.txt)
# Author: Zoe McNamara Harlowe

FILENAME = "count.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
def write_number(number):
    with open(FILENAME, "wt") as f:
        new_number = f.write(str(number))

num = read_number() 
num += 1

write_number(num)

print(f"We have run this program {num} times")

import os

if os.path.exists("count.txt") == True:
    print("This file exists")
else:
    print("This file doesn't exist")
    write_number(0)

