# normalise.py
# This program will read in a string and output it in lowercase
# It will also strip any leading or trailing spaces and say the 
# length of the input and output strings
# Author: Zoe McNamara Harlowe

input_string = input("Please enter a string: ")
normalised_string = (input_string.strip().lower())
input_length = len(input_string)
output_length = len(normalised_string)

print("That string normalised is: " + normalised_string)

# I had to cast the lengths as strings to concatenate them
print("We reduced the input string from " + str(input_length) + " to " + str(output_length) + " charachters")
