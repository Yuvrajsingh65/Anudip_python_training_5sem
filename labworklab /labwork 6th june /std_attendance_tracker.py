'''
6. Student Attendance Tracker 
Problem Statement 
Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent. 
'''
# List showing attendance for 15 days
# P = Present
# A = Absent

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count Present and Absent Days
present = 0
absent = 0

# Check each day's attendance
for day in attendance:

    # If student is present
    if day == 'P':
        present += 1

    # Otherwise student is absent
    else:
        absent += 1

print("Present Days =", present)
print("Absent Days =", absent)

# Calculate Attendance Percentage
# Total number of days
total_days = len(attendance)

# Formula for attendance percentage
percentage = (present / total_days) * 100

print("Attendance Percentage =", percentage, "%")

# Check Eligibility

# Student is eligible if attendance is 75% or more
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Display Absent Positions
print("Absent on Day Numbers:")

# Check attendance with position
for i in range(len(attendance)):

    # If absent, print day number
    if attendance[i] == 'A':
        print(i + 1)
