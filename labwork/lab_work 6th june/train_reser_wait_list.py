'''
10. Train Reservation Waiting List 
Problem Statement 
Passenger records: 
passengers = [ 
    ("Anuj", "Confirmed"), 
    ("Rahul", "Waiting"), 
    ("Priya", "Confirmed"), 
    ("Amit", "Waiting"), 
    ("Neha", "Confirmed") 
] 
Write a program to: 
• Display all waiting-list passengers.  
• Count confirmed and waiting passengers.  
• Find whether a specific passenger has a confirmed ticket.  
• Create separate lists for confirmed and waiting passengers.
'''
# Passenger records with booking status
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Display Waiting List Passengers

print("Waiting List Passengers:")

for name, status in passengers:
    if status == "Waiting":
        print(name)

# Count Confirmed and Waiting Passengers
confirmed_count = 0
waiting_count = 0

for name, status in passengers:
    if status == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("\nConfirmed Passengers =", confirmed_count)
print("Waiting Passengers =", waiting_count)

# Check Whether a Passenger is Confirmed
search_name = "Priya"

for name, status in passengers:
    if name == search_name and status == "Confirmed":
        print("\n", search_name, "has a Confirmed Ticket")
        break

# Create Separate Lists

confirmed_list = []
waiting_list = []

for name, status in passengers:

    if status == "Confirmed":
        confirmed_list.append(name)

    else:
        waiting_list.append(name)

print("\nConfirmed List =", confirmed_list)
print("Waiting List =", waiting_list)
