# do_add.py
# This program is used to test part of students.py
# Author: Zoe McNamara Harlowe
modules = []
students = []

def read_modules(): 
    modules = [] 
    module_name = input("\tEnter the first module name (blank to quit): ").strip() 
     
    while module_name != "": 
        module = {} 
        module["Name"]= module_name  
        module["Grade"]=int(input("\t\tEnter grade:")) 
        modules.append(module) 
        module_name = input("\tEnter next module name (blank to quit): ").strip() 
 
    return modules

def do_add(students):
    current_student = {}
    current_student["Name"] = input("Enter student name: ")
    current_student["Modules"] = read_modules() 

    students.append(current_student)
    return students
    
do_add(students)
print(students)
