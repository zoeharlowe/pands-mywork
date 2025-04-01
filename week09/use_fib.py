# use_fib.py
# This program uses the fibonacci() module (from AndrewsmyFunctions.py) to prompt 
# a user for a number and will return the list of the Fibonacci sequence
# Author: Zoe McNamara Harlowe

import AndrewsmyFunctions as mf

number = int(input("Please enter a number: "))
print(mf.fibonacci(number))