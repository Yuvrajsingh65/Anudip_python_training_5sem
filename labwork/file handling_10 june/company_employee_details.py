'''
Constraints 
• Use functions to modularize the program.  
• Use file handling (open(), read(), write(), append()).  
• Use lists/dictionaries wherever appropriate.  
• Do not use databases or external libraries.  
• Implement menu-driven execution using a while loop.  
• Ensure that updates are reflected in the original file. ------------------------------------------------------------------------------------------------------------------------- 
1. Employee Payroll Management System 
Problem Statement 
A company stores employee details in a text file named employees.txt. 
File Format 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Requirements 
Create a menu-driven program to: 
1. Display all employee records.  
2. Search employee details using Employee ID.  
3. Calculate the average salary.  
4. Find the highest-paid and lowest-paid employee.  
5. Display employees earning above ₹50,000.  
6. Add a new employee record to the file.  
7. Generate salary categories:  
o High (₹60,000 and above)  
o Medium (₹40,000-₹59,999)  
o Low (Below ₹40,000) 
'''
# Employee Payroll Management System

# Function to read employee data from file
def read_data():
    employees = []

    file = open("employees.txt", "r")

    for line in file:
        data = line.strip().split(",")

        emp_id = data[0]
        name = data[1]
        salary = int(data[2])

        employees.append([emp_id, name, salary])

    file.close()
    return employees


# Function to display all employees
def display_all():
    employees = read_data()

    print("\nEmployee Records")
    for emp in employees:
        print(emp[0], emp[1], emp[2])


# Function to search employee by ID
def search_employee():
    employees = read_data()

    eid = input("Enter Employee ID: ")

    found = False

    for emp in employees:
        if emp[0] == eid:
            print("ID:", emp[0])
            print("Name:", emp[1])
            print("Salary:", emp[2])
            found = True

    if found == False:
        print("Employee not found")


# Function to calculate average salary
def average_salary():
    employees = read_data()

    total = 0

    for emp in employees:
        total = total + emp[2]

    avg = total / len(employees)

    print("Average Salary =", avg)


# Function to find highest and lowest salary
def highest_lowest():
    employees = read_data()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:

        if emp[2] > highest[2]:
            highest = emp

        if emp[2] < lowest[2]:
            lowest = emp

    print("Highest Paid Employee:")
    print(highest[0], highest[1], highest[2])

    print("Lowest Paid Employee:")
    print(lowest[0], lowest[1], lowest[2])


# Function to display salary above 50000
def above_50000():
    employees = read_data()

    print("\nEmployees earning above 50000")

    for emp in employees:
        if emp[2] > 50000:
            print(emp[0], emp[1], emp[2])


# Function to add new employee
def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee Added Successfully")


# Function to display salary category
def salary_category():
    employees = read_data()

    for emp in employees:

        if emp[2] >= 60000:
            category = "High"

        elif emp[2] >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(emp[0], emp[1], emp[2], "->", category)


# Main Menu
while True:

    print("\n----- Employee Payroll Management -----")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above 50000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_all()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest()

    elif choice == 5:
        above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_category()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
