'''
Employee Performance Evaluation
Problem statement
A company stores employee details in a tuple. Each employee record contains: 
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
Where: 
• First value = Employee ID  
• Second value = Employee Name  
• Third value = Performance Score  
Tasks 
Write a Python program to: 
1. Display details of employees scoring 80 or above.  
2. Count the number of employees who need improvement (score below 60).  
3. Find the employee with the highest score.  
4. Create a list containing the names of all employees scoring above 75.  
5. Display the performance category for each employee:  
o 90 and above → Excellent  
o 75 to 89 → Good  
o 60 to 74 → Average  
o Below 60 → Needs Improvement
'''
# Employee data stored in a tuple
# Format: (Employee ID, Employee Name, Performance Score)

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# ---------------------------------------------------
# 1. Display employees who scored 80 or more
# ---------------------------------------------------

print("Employees scoring 80 or above:")

# Check each employee one by one
for emp in employees:

    # emp[2] contains the score
    if emp[2] >= 80:
        print(emp)

# 2. Count employees who need improvement(score less than 60)

count = 0   # Variable to store number of employees

for emp in employees:

    # If score is below 60, increase count by 1
    if emp[2] < 60:
        count = count + 1

print("\nEmployees needing improvement =", count)

# ---------------------------------------------------
# 3. Find employee with highest score
# ---------------------------------------------------

# Assume first employee has highest score
highest = employees[0]

for emp in employees:

    # Compare current employee score with highest score
    if emp[2] > highest[2]:
        highest = emp

print("\nEmployee with highest score:")
print(highest)

# ---------------------------------------------------
# 4. Create a list of employee names
#    whose score is greater than 75
# ---------------------------------------------------

name_list = []   # Empty list

for emp in employees:

    # Add employee name to list if score > 75
    if emp[2] > 75:
        name_list.append(emp[1])

print("\nNames of employees scoring above 75:")
print(name_list)

# ---------------------------------------------------
# 5. Display performance category
# ---------------------------------------------------

print("\nPerformance Category of Employees:")

for emp in employees:

    score = emp[2]

    # Decide category based on score
    if score >= 90:
        print(emp[1], "-> Excellent")

    elif score >= 75:
        print(emp[1], "-> Good")

    elif score >= 60:
        print(emp[1], "-> Average")

    else:
        print(emp[1], "-> Needs Improvement")
                                   
