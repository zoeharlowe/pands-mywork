# student.py
# This program will store a student name and a list of courses and grades for each course
# It will then output the student's data
# Author: Zoe McNamara Harlowe

# Create a dictionary called student_profile
# There is a dictionary object within the dictionary called "Courses"
student_profile = {
    "name" : "Mary",
    "Courses" : [
        { 
        "course_name" : "Programming",
        "grade" : 45,
        },
        {
        "course_name" : "History",
        "grade" : 99,
        }
        ]
}

print("Student:", student_profile["name"])

# For loop to output the course name and grade for each course
for course in student_profile["Courses"]:
    print("\t", course["course_name"], ":", "\t", course["grade"])