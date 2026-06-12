'''
Problem 6: Library Book Availability System 
Problem Statement 
The number of available copies of books in a library is stored below. 
Sample Data 
books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
Tasks 
1. Display books with fewer than 3 copies.  
2. Find the book with maximum copies.  
3. Find the book with minimum copies.  
4. Count total books available.  
5. Generate a restocking list. 
'''
# Library Book Availability System

# Dictionary to store book names and available copies
books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

# Task 1: Display books with fewer than 3 copies
print("Books with fewer than 3 copies:")
for book in books:
    if books[book] < 3:
        print(book, ":", books[book])

# Task 2: Find the book with maximum copies
max_book = max(books, key=books.get)
print("\nBook with Maximum Copies:")
print(max_book, ":", books[max_book])

# Task 3: Find the book with minimum copies
min_book = min(books, key=books.get)
print("\nBook with Minimum Copies:")
print(min_book, ":", books[min_book])

# Task 4: Calculate total number of book copies available
total_copies = sum(books.values())
print("\nTotal Books Available:", total_copies)

# Task 5: Generate a restocking list
# Books having less than 3 copies need restocking
restocking_list = []

for book in books:
    if books[book] < 3:
        restocking_list.append(book)

print("\nBooks to be Restocked:")
print(restocking_list)
