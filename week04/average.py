# average.py
# This program keeps reading in numbers until the user inputs a 0
# It will then print back out the numbers entered and the average of those numbers
# Author: Zoe McNamara Harlowe

# I used GeeksforGeeks to help me find an average of a list using a for loop
# https://www.geeksforgeeks.org/find-average-list-python/

numbers = []

# Initialise total sum to 0

total_sum = 0

# Iterate over each element in list and accumulate sum

number = int(input("Enter a number (0 to quit): "))
while number != 0:
    numbers.append(number)
    number = int(input("Enter another number (0 to quit): "))
for val in numbers:
    total_sum += val

# Calculate average by dividing total sum by length of list
# I want average to be a float
average = float(total_sum / len(numbers))

print("The numbers you entered were: ", numbers)
print("The average of those numbers is: ", average)