'''
Question 2: Flight Booking Analysis 
Problem Statement 
A flight reservation system stores passenger records as tuples: 
bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
) 
Where: 
• Passenger ID  
• Destination  
• Booking Status  
Tasks 
Write a Python program to: 
1. Display all passengers whose booking status is Confirmed.  
2. Count the number of passengers travelling to Delhi.  
3. Count Confirmed, Waiting, and Cancelled bookings separately.  
4. Create a list containing passenger IDs with Waiting status.  
5. Determine which destination has the highest number of bookings.  
'''
# Flight booking records are stored in a tuple.
# Each record contains:
# (Passenger ID, Destination, Booking Status)

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# ==================================================
# TASK 1: Display all passengers whose booking
# status is "Confirmed"
# ==================================================

print("Confirmed Passengers:")

# Read each booking record one by one
for booking in bookings:

    # Check if booking status is Confirmed
    if booking[2] == "Confirmed":

        # Print complete passenger record
        print(booking)

# ==================================================
# TASK 2: Count passengers travelling to Delhi
# ==================================================

# Variable to store count of Delhi passengers
delhi_count = 0

# Check every booking
for booking in bookings:

    # If destination is Delhi
    if booking[1] == "Delhi":

        # Increase count by 1
        delhi_count = delhi_count + 1

# Display total count
print("\nPassengers travelling to Delhi =", delhi_count)

# ==================================================
# TASK 3: Count Confirmed, Waiting and Cancelled
# bookings separately
# ==================================================

# Variables to store counts
confirmed = 0
waiting = 0
cancelled = 0

# Read every booking record
for booking in bookings:

    # Check booking status

    if booking[2] == "Confirmed":
        confirmed = confirmed + 1

    elif booking[2] == "Waiting":
        waiting = waiting + 1

    elif booking[2] == "Cancelled":
        cancelled = cancelled + 1

# Display counts
print("\nConfirmed Bookings =", confirmed)
print("Waiting Bookings =", waiting)
print("Cancelled Bookings =", cancelled)

# ==================================================
# TASK 4: Create a list of Passenger IDs whose
# booking status is Waiting
# ==================================================

# Empty list to store passenger IDs
waiting_ids = []

# Read each booking
for booking in bookings:

    # If status is Waiting
    if booking[2] == "Waiting":

        # Add Passenger ID to the list
        waiting_ids.append(booking[0])

# Display list
print("\nPassenger IDs with Waiting Status:")
print(waiting_ids)

# ==================================================
# TASK 5: Find destination with highest bookings
# ==================================================

# Count bookings for each city
delhi = 0
mumbai = 0
chennai = 0

# Read every booking
for booking in bookings:

    # Count destination bookings

    if booking[1] == "Delhi":
        delhi = delhi + 1

    elif booking[1] == "Mumbai":
        mumbai = mumbai + 1

    elif booking[1] == "Chennai":
        chennai = chennai + 1

# Compare counts and find highest

if delhi > mumbai and delhi > chennai:
    print("\nDestination with Highest Bookings = Delhi")

elif mumbai > delhi and mumbai > chennai:
    print("\nDestination with Highest Bookings = Mumbai")

else:
    print("\nDestination with Highest Bookings = Chennai")
