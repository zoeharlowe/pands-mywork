# student2.py
# This program reads in a student's courses and grades until the user enters a blank
# It will then output the data
# Author: Zoe McNamara Harlowe

# Create 2 lists to store the courses and grades
list_of_courses = []
list_of_grades = []

# Initialise the input_course_name variable to an empty string
input_course_name = str(input)

# Create while loop to get the program to continue running until the user inputs a blank
while len(input_course_name) != 0:
    input_course_name = str(input("Enter course name: "))
    list_of_courses.append(input_course_name)
    if len(input_course_name) == 0:
        break
    input_grade = str(input("Enter grade: "))

# Create a dictionary called student_profile to store the data  
# I wasn't sure what the best way of representing the courses and grades was
student_profile = {
    "name" : str(input("Enter student name: ")),
    "Courses" : [
            { 
    "course_name" : list_of_courses,
    "grade" : list_of_grades,
            },
            ]
    }

print("Student:", student_profile["name"])

# Check to see if the courses and grades are being stored correctly
# The courses are, the grades are not
print(list_of_courses)
print(list_of_grades)

# I used a for loop to output the course name and grade for each course
# Unfortunately I couldn't get this to print any courses or grades
for course in student_profile["Courses"]:
    for i in range(len(list_of_courses)) and range(len(list_of_grades)):
        print("\t", list_of_courses[i], ":", "\t", list_of_grades[i])
