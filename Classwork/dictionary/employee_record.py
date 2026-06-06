# Create an empty dictionary
employees = {}

# Input records of 10 employees
for i in range(10):
    emp_id = input("Enter Employee ID: ")
    salary = int(input("Enter Salary: "))
    
    # Store employee ID as key and salary as value
    employees[emp_id] = salary

# Variable to count employees having salary greater than 30000
count = 0

# List to store employee IDs having salary below 20000
low_salary_emp = []

# Check salaries
for emp_id, salary in employees.items():
    
    if salary > 30000:
        count += 1
        
    if salary < 20000:
        low_salary_emp.append(emp_id)

# Display results
print("\nTotal employees having salary greater than 30000 =", count)

print("\nEmployees having salary below 20000:")
for emp_id in low_salary_emp:
    print(emp_id)
