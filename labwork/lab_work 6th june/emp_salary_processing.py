'''
4. Employee Salary Processing 
Problem Statement 
Employee data is stored as tuples: 
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000. 
'''
# List of employees with their salaries
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Display employees earning above ₹50,000
print("Employees earning above ₹50,000:")

# Check each employee's salary
for name, salary in employees:
    if salary > 50000:
        print(name, "-", salary)

# Find the highest-paid employee
# Assume first employee has highest salary
highest_name = employees[0][0]
highest_salary = employees[0][1]

# Compare salaries
for name, salary in employees:
    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

print("\nHighest-Paid Employee:")
print(highest_name, "-", highest_salary)

# Calculate total salary expenditure
total_salary = 0

# Add all salaries
for name, salary in employees:
    total_salary = total_salary + salary

print("\nTotal Salary Expenditure =", total_salary)

# Count employees earning below ₹40,000

count = 0

# Check each employee's salary
for name, salary in employees:
    if salary < 40000:
        count = count + 1

print("\nEmployees earning below ₹40,000 =", count)
