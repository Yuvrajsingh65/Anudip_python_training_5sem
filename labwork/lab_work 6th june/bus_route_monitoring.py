'''
8. Bus Route Monitoring 
Problem Statement 
Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] 
Write a program to: 
• Find the busiest stop.  
• Display stops with fewer than 10 passengers.  
• Calculate average passengers.  
• Determine whether any stop exceeded 25 passengers. 
'''
# Number of passengers at each bus stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find the Busiest Stop

# Find maximum passengers
busiest = max(passengers)

print("Busiest Stop Passengers =", busiest)

# Display Stops with Fewer than 10 Passengers

print("\nStops with fewer than 10 passengers:")

# Check each stop
for i in range(len(passengers)):

    # If passengers are less than 10
    if passengers[i] < 10:
        print("Stop", i + 1, "=", passengers[i], "passengers")

# Calculate Average Passengers

# Add all passenger counts
total = sum(passengers)

# Calculate average
average = total / len(passengers)

print("\nAverage Passengers =", average)

# Check if Any Stop Exceeded 25 Passengers
found = False

# Check each stop
for count in passengers:

    # If passengers are more than 25
    if count > 25:
        found = True
        break

if found:
    print("\nYes, a stop exceeded 25 passengers.")
else:
    print("\nNo stop exceeded 25 passengers.")
