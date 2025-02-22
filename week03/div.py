# div.py
# This program reads in two numbers and divides the first one by the second one and gives the integer result and the remainder
# Author: Zoe McNamara Harlowe

first_number = int(input("Enter first number: "))
second_number = int(input("Enter number you want to divide by: "))

answer = first_number // second_number 
remainder = first_number % second_number

print(f"{first_number} divided by {second_number} is {answer} with remainder {remainder}")