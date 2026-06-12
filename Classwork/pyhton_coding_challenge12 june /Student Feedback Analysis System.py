'''
Problem 11: Student Feedback Analysis System 
Problem Statement 
A training institute collects feedback from students after completing a Python course. The feedback 
comments are stored in a text file named feedback.txt. 
Sample Input/Data (feedback.txt) 
The sessions were very interactive and informative. 
Excellent teaching methodology and practical examples. 
The pace of the course was appropriate. 
More real-world projects should be included. 
The trainer explained concepts very clearly. 
Tasks 
1. Count the total number of lines.  
2. Count the total number of words.  
3. Count the total number of characters.  
4. Find the longest feedback comment.  
5. Find the shortest feedback comment.  
6. Count the total number of vowels present in the file. 
'''
# Student Feedback Analysis System

# Open the file in read mode
file = open("feedback.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Close the file
file.close()

# Task 1: Count total number of lines
total_lines = len(lines)

print("Total Number of Lines =", total_lines)

# Task 2: Count total number of words
word_count = 0

for line in lines:
    words = line.split()
    word_count = word_count + len(words)

print("Total Number of Words =", word_count)

# Task 3: Count total number of characters
char_count = 0

for line in lines:
    char_count = char_count + len(line)

print("Total Number of Characters =", char_count)

# Task 4: Find the longest feedback comment
longest = max(lines, key=len)

print("\nLongest Feedback Comment:")
print(longest)

# Task 5: Find the shortest feedback comment
shortest = min(lines, key=len)

print("Shortest Feedback Comment:")
print(shortest)

# Task 6: Count total number of vowels in the file
vowel_count = 0

for line in lines:
    for ch in line.lower():
        if ch in "aeiou":
            vowel_count = vowel_count + 1

print("Total Number of Vowels =", vowel_count)
