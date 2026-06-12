'''
Problem 2: Student Scholarship Evaluation System 
Problem Statement 
The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90). 
'''
# Student Scholarship Evaluation System

# Dictionary containing student names and their marks
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# 1. Display students who scored more than 85 marks
print("Students scoring above 85 marks:")

for student in marks:
    if marks[student] > 85:
        print(student, "=", marks[student])

# 2. Find the topper (highest marks)
topper = max(marks, key=marks.get)

print("\nTopper of the class:")
print(topper, "=", marks[topper])

# 3. Find the student with the lowest marks
lowest = min(marks, key=marks.get)

print("\nStudent with lowest marks:")
print(lowest, "=", marks[lowest])

# 4. Calculate the average marks of the class
total = sum(marks.values())      # Add all marks
average = total / len(marks)     # Divide by total number of students

print("\nClass Average =", average)

# 5. Generate grades for each student
print("\nGrades of Students:")

for student in marks:

    # Assign grade according to marks
    if marks[student] >= 90:
        grade = "A"

    elif marks[student] >= 75:
        grade = "B"

    elif marks[student] >= 50:
        grade = "C"

    else:
        grade = "F"

    print(student, ":", grade)

# 6. Create a list of scholarship students
# Scholarship is given to students scoring 90 or more marks

scholarship_students = []

for student in marks:
    if marks[student] >= 90:
        scholarship_students.append(student)

print("\nScholarship Students:")
print(scholarship_students)
