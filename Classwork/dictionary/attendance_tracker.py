'''
Create Attendance tracker of 30 students. Ask the user to input roll number of student and also 
input whether student is Present or Absent. Store the data in dictionary where roll number will 
be used as a key and Attendance as Value. 
Display the roll number of students who are Present
'''
# Create an empty dictionary to store attendance
attendance = {}

# Input attendance of 30 students
for i in range(30):

    # Input roll number
    roll_no = input("Enter Roll Number: ")

    # Input attendance status (P for Present, A for Absent)
    status = input("Enter Attendance (P/A): ")

    # Store data in dictionary
    attendance[roll_no] = status

# Display Present Students

print("\nStudents who are Present:")

# Check each student's attendance
for roll_no in attendance:

    # If student is present
    if attendance[roll_no] == "P":
        print(roll_no)  
  
