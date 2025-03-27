# student.py
# This program allows a user to create and view new students, along with their modules and grades
# Author: Zoe McNamara Harlowe

def display_menu():
    print("What would you like to do?" "\n" "\t" "(a) Add new student" "\n" "\t" 
          "(v) View students" "\n" "\t" "(s) Save" "\n" "\t" "(q) Quit")
    choice = input("Type one letter: ").strip()
    print(f"You chose {choice}")
    return choice


students = []

def read_modules(): 
    modules = [] 
    module_name = input("\tEnter the first module name (blank to quit): ").strip() 
    # While loop to read in multiple modules and grades
    while module_name != "": 
        module = {} 
        module["Name"]= module_name  
        module["Grade"]=int(input("\t\tEnter grade: ")) 
        # Each module gets appended to the list 'modules'
        modules.append(module) 
        module_name = input("\tEnter next module name (blank to quit): ").strip() 
 
    return modules

def do_add(students):
    current_student = {}
    current_student["Name"] = input("Enter student name: ")
    current_student["Modules"] = read_modules() 

    students.append(current_student)
    return students

def display_modules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{ module["Name"]} \t{ module['Grade']}")


def do_view(students):
    for current_student in students:
        print(current_student["Name"])
        display_modules(current_student["Modules"])

# Main program

students = []
choice = display_menu()

while choice != "q":
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice != "q":
        print("Please enter either a, v or q")
    choice = display_menu()
