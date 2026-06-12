'''
Problem 20: Employee Performance Evaluation System 
Problem Statement 
Employee performance scores are stored below. 
Sample Data 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Categorize employees:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60) 
'''
# Employee Performance Evaluation System

# Dictionary storing employee ID and performance score
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Task 1: Display employees scoring above 80
print("Employees Scoring Above 80:")

for emp in performance:
    if performance[emp] > 80:
        print(emp, ":", performance[emp])

# Task 2: Count employees needing improvement
# Employees with score less than 60 need improvement
count = 0

for score in performance.values():
    if score < 60:
        count = count + 1

print("\nEmployees Needing Improvement:", count)

# Task 3: Find the top performer
top_performer = max(performance, key=performance.get)

print("\nTop Performer:")
print(top_performer, ":", performance[top_performer])

# Task 4: Calculate average performance score
average_score = sum(performance.values()) / len(performance)

print("\nAverage Performance Score =", average_score)

# Task 5: Categorize employees
print("\nEmployee Categories:")

for emp in performance:

    # Excellent category
    if performance[emp] >= 90:
        category = "Excellent"

    # Good category
    elif performance[emp] >= 75:
        category = "Good"

    # Average category
    elif performance[emp] >= 60:
        category = "Average"

    # Poor category
    else:
        category = "Poor"

    print(emp, ":", category)
