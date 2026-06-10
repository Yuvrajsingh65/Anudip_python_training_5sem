'''
2. Library Book Issue System 
Problem Statement 
A library stores book information in books.txt. 
File Format 
B101,Python Basics,5 
B102,Java Programming,2 
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1 
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3 
Requirements 
Develop a program to: 
1. Display all books.  
2. Search a book using Book ID.  
3. Issue a book (decrease quantity by 1).  
4. Return a book (increase quantity by 1).  
5. Display unavailable books.  
6. Display books requiring restocking (copies < 2).  
7. Update the file after every issue/return operation.
'''
# Library Book Issue System

# Function to read books from file
def read_books():
    books = []

    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")

        book_id = data[0]
        book_name = data[1]
        quantity = int(data[2])

        books.append([book_id, book_name, quantity])

    file.close()
    return books


# Function to save updated data into file
def save_books(books):

    file = open("books.txt", "w")

    for book in books:
        file.write(book[0] + "," + book[1] + "," + str(book[2]) + "\n")

    file.close()


# Function to display all books
def display_books():

    books = read_books()

    print("\nBook Records")
    for book in books:
        print(book[0], book[1], book[2])


# Function to search a book
def search_book():

    books = read_books()

    bid = input("Enter Book ID: ")

    found = False

    for book in books:

        if book[0] == bid:
            print("Book ID :", book[0])
            print("Book Name :", book[1])
            print("Quantity :", book[2])
            found = True

    if found == False:
        print("Book not found")


# Function to issue a book
def issue_book():

    books = read_books()

    bid = input("Enter Book ID to issue: ")

    for book in books:

        if book[0] == bid:

            if book[2] > 0:
                book[2] = book[2] - 1
                save_books(books)
                print("Book Issued Successfully")
            else:
                print("Book Not Available")

            return

    print("Book ID not found")


# Function to return a book
def return_book():

    books = read_books()

    bid = input("Enter Book ID to return: ")

    for book in books:

        if book[0] == bid:
            book[2] = book[2] + 1
            save_books(books)
            print("Book Returned Successfully")
            return

    print("Book ID not found")


# Function to display unavailable books
def unavailable_books():

    books = read_books()

    print("\nUnavailable Books")

    for book in books:
        if book[2] == 0:
            print(book[0], book[1])


# Function to display books requiring restocking
def restocking_books():

    books = read_books()

    print("\nBooks Requiring Restocking")

    for book in books:
        if book[2] < 2:
            print(book[0], book[1], "Quantity =", book[2])


# Main Menu
while True:

    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
