'''
Problem 12: Employee Salary Report Generator 
Problem Statement 
Employee details are stored in a text file named employees.txt. 
Sample Input/Data (employees.txt) 
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
Tasks 
1. Display employees earning more than ₹50,000.  
2. Find the highest-paid employee.  
3. Find the lowest-paid employee.  
4. Calculate the average salary.  
5. Generate salary categories:  
o High (≥ ₹60,000)  
o Medium (₹40,000 – ₹59,999)  
o Low (< ₹40,000)  
'''
# Employee Salary Report Generator

# Open the file in read mode
file = open("employees.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Close the file
file.close()

# Create empty lists to store employee data
names = []
salaries = []

# Extract name and salary from each line
for line in lines:
    data = line.strip().split(",")

    names.append(data[1])          # Employee name
    salaries.append(int(data[2]))  # Employee salary

# Task 1: Display employees earning more than 50000
print("Employees Earning More Than ₹50,000:")

for i in range(len(names)):
    if salaries[i] > 50000:
        print(names[i], ":", salaries[i])

# Task 2: Find the highest-paid employee
max_salary = max(salaries)
index = salaries.index(max_salary)

print("\nHighest Paid Employee:")
print(names[index], ":", max_salary)

# Task 3: Find the lowest-paid employee
min_salary = min(salaries)
index = salaries.index(min_salary)

print("\nLowest Paid Employee:")
print(names[index], ":", min_salary)

# Task 4: Calculate average salary
average_salary = sum(salaries) / len(salaries)

print("\nAverage Salary =", average_salary)

# Task 5: Generate salary categories

print("\nSalary Categories:")

for i in range(len(names)):

    # High salary category
    if salaries[i] >= 60000:
        category = "High"

    # Medium salary category
    elif salaries[i] >= 40000:
        category = "Medium"

    # Low salary category
    else:
        category = "Low"

    print(names[i], ":", category)
