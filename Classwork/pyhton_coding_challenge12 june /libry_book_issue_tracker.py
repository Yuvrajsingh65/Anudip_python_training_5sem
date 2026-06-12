'''
Problem 13: Library Book Issue Tracker 
Problem Statement 
A library stores the number of times books were issued during a month. 
Sample Data 
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 
Tasks 
1. Find the maximum number of issues.  
2. Find the minimum number of issues.  
3. Calculate the average number of issues.  
4. Count books issued more than 15 times.  
5. Create a list of books issued fewer than 10 times. 
'''
# Library Book Issue Tracker

# List containing the number of times books were issued
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# 1. Find the maximum number of issues
# max() returns the largest value from the list
print("Maximum Issues =", max(book_issues))

# 2. Find the minimum number of issues
# min() returns the smallest value from the list
print("Minimum Issues =", min(book_issues))

# 3. Calculate the average number of issues
# sum() adds all values and len() gives total values
average = sum(book_issues) / len(book_issues)

print("Average Issues =", average)

# 4. Count books issued more than 15 times
count = 0

# Check each value in the list
for issues in book_issues:
    if issues > 15:
        count = count + 1

print("Books Issued More Than 15 Times =", count)

# 5. Create a list of books issued fewer than 10 times
low_issue_books = []

# Check each value and store values less than 10
for issues in book_issues:
    if issues < 10:
        low_issue_books.append(issues)

print("Books Issued Fewer Than 10 Times:")
print(low_issue_books)
