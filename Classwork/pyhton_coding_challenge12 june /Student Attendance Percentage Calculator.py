'''
Problem 18: Student Attendance Percentage Calculator 
Problem Statement 
The attendance status of a student for 15 days is represented as follows: 
Sample Data 
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 
Tasks 
1. Count present days.  
2. Count absent days.  
3. Calculate attendance percentage.  
4. Determine whether attendance is below 75%.  
5. Display the attendance status.
'''
# Student Attendance Percentage Calculator

# Tuple storing attendance status
# P = Present, A = Absent
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

# Task 1: Count present days
present_days = attendance.count('P')

print("Present Days =", present_days)

# Task 2: Count absent days
absent_days = attendance.count('A')

print("Absent Days =", absent_days)

# Task 3: Calculate attendance percentage
total_days = len(attendance)

attendance_percentage = (present_days / total_days) * 100

print("Attendance Percentage =", attendance_percentage, "%")

# Task 4: Check whether attendance is below 75%
if attendance_percentage < 75:
    print("Attendance is below 75%")
else:
    print("Attendance is 75% or above")

# Task 5: Display attendance status
print("Attendance Status:")
print(attendance)
