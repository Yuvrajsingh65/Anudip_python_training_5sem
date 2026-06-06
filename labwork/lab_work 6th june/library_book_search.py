'''
5. Library Book Search 
Problem Statement 
Books available in a library: 
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 
Write a program to: 
• Display unavailable books.  
• Find all books with more than 2 copies.  
• Count available books.  
• Stop searching once a requested book is found. 
'''
# List of books and number of copies available
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")

# Check each book
for book, copies in books:
    
    # If copies are 0, book is unavailable
    if copies == 0:
        print(book)

# Find books with more than 2 copies
print("\nBooks with more than 2 copies:")

# Check each book
for book, copies in books:
    
    # If copies are greater than 2
    if copies > 2:
        print(book)

# Count available books
count = 0

# Count books having at least 1 copy
for book, copies in books:
    
    if copies > 0:
        count = count + 1

print("\nAvailable Books =", count)

# Stop searching when book is found
# Book to search
search_book = "Java Programming"

# Check each book
for book, copies in books:
    
    # If book is found
    if book == search_book:
        print("\nBook Found:", book)
        
        # Stop the loop immediately
        break
