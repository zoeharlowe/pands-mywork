# grade.py
# This program will read in a student's percentage mark and output the corresponding grade
# Author: Zoe McNamara Harlowe

grade = float(input("Please enter the percentage mark: "))

# I made an if statement to ensure that the number inputted would be a valid percentage
# I then made numerous elif statements for each grade boundary
# I used an else statement to output 'Fail' if the number was below 40
if grade < 0 or grade > 100:
    print("Please enter a valid percentage mark")
elif grade >= 70:
    print("Distinction")
elif grade >= 60 and grade < 70:
    print("Merit 1")
elif grade >= 50 and grade < 60:
    print("Merit 2")
elif grade >= 40 and grade < 50:
    print("Pass")
else: 
    print("Fail")