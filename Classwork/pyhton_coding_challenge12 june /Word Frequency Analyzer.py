'''
Problem 19: Word Frequency Analyzer 
Problem Statement 
A text file contains the following paragraph. 
Sample Input/Data (article.txt) 
Python is easy to learn. 
Python is powerful. 
Python supports multiple programming paradigms. 
Programming with Python is enjoyable. 
Tasks 
1. Count the total number of words.  
2. Count the frequency of each word.  
3. Find the most frequently occurring word.  
4. Display words appearing only once.  
5. Display all unique words.  
'''
# Word Frequency Analyzer

# Open the file in read mode
file = open("article.txt", "r")

# Read complete file content
text = file.read()

# Close the file
file.close()

# Convert text to lowercase and split into words
words = text.lower().split()

# Task 1: Count total number of words
total_words = len(words)

print("Total Number of Words =", total_words)

# Task 2: Count frequency of each word
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for word in frequency:
    print
