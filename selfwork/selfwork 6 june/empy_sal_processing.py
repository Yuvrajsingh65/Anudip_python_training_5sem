'''
3. Employee Salary Processing 
Sample Data 
salary = { 
    "EMP101": 45000, 
    "EMP102": 62000, 
    "EMP103": 38000, 
    "EMP104": 75000, 
    "EMP105": 54000, 
    "EMP106": 29000, 
    "EMP107": 82000, 
    "EMP108": 48000, 
    "EMP109": 36000, 
    "EMP110": 68000 
} 
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary. 
'''
# Dictionary containing Employee ID and Salary

salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Display employees earning above ₹60,000

print("Employees earning above ₹60,000:")

for emp in salary:
    if salary[emp] > 60000:
        print(emp, ":", salary[emp])

# Count employees earning below ₹40,000

count = 0

for emp in salary:
    if salary[emp] < 40000:
        count += 1

print("\nEmployees earning below ₹40,000 =", count)

# Find the highest-paid employee

highest_emp = max(salary, key=salary.get)

print("\nHighest Paid Employee:")
print(highest_emp, ":", salary[highest_emp])

# Create list of employees eligible
# for bonus (salary > ₹50,000)
bonus_list = []

for emp in salary:
    if salary[emp] > 50000:
        bonus_list.append(emp)

print("\nEmployees Eligible for Bonus:")
print(bonus_list)

# Calculate Average Salary

total_salary = 0

for emp in salary:
    total_salary += salary[emp]

average_salary = total_salary / len(salary)

print("\nAverage Salary =", average_salary)
