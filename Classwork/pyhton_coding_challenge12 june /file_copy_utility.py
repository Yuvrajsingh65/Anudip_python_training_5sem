Problem 16: File Copy Utility 
Problem Statement 
A company wants to maintain backups of important documents. Create a program to copy the contents of 
one file into another.
Sample Input/Data 
Source File (notes.txt) 
Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs. 
Tasks 
1. Read the contents of the source file.  
2. Copy the entire content to another file named backup.txt.  
3. Display a success message.  
4. Verify whether both files contain the same number of lines. 
'''
# File Copy Utility

# Task 1: Open the source file in read mode
source_file = open("notes.txt", "r")

# Read all contents from the source file
data = source_file.read()

# Close the source file
source_file.close()

# Task 2: Open backup file in write mode
backup_file = open("backup.txt", "w")

# Copy the contents into backup file
backup_file.write(data)

# Close the backup file
backup_file.close()

# Task 3: Display success message
print("File copied successfully!")

# Task 4: Verify whether both files have the same number of lines

# Open source file and read lines
source_file = open("notes.txt", "r")
source_lines = source_file.readlines()
source_file.close()

# Open backup file and read lines
backup_file = open("backup.txt", "r")
backup_lines = backup_file.readlines()
backup_file.close()

# Compare number of lines in both files
if len(source_lines) == len(backup_lines):
    print("Both files contain the same number of lines.")
else:
    print("Files do not contain the same number of lines.")
