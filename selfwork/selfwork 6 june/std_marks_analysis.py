'''
1. Student Marks Analysis 
Sample Data 
marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
o A: ≥ 90  
o B: 75–89  
o C: 50–74  
o F: < 50 1.
'''
# Dictionary containing student names and marks
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}
# Display students scoring 80 or above
print("Students scoring 80 or above:")

for name in marks:
    if marks[name] >= 80:
        print(name, ":", marks[name])

# Count failed students
fail_count = 0

for name in marks:
    if marks[name] < 40:
        fail_count += 1

print("\nNumber of Failed Students =", fail_count)

# Find highest scorer

highest_student = max(marks, key=marks.get)

print("\nHighest Scorer =", highest_student)
print("Marks =", marks[highest_student])

# Create list of students scoring
# between 60 and 75
student_list = []

for name in marks:
    if marks[name] >= 60 and marks[name] <= 75:
        student_list.append(name)

print("\nStudents scoring between 60 and 75:")
print(student_list)

# Assign Grades

print("\nStudent Grades:")

for name in marks:

    if marks[name] >= 90:
        grade = "A"

    elif marks[name] >= 75:
        grade = "B"

    elif marks[name] >= 50:
        grade = "C"

    else:
        grade = "F"

    print(name, ":", grade)
