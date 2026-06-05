# List representing the seats in the bus
# 1 means the seat is booked
# 0 means the seat is available
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# -----------------------------------------
# 1. Count booked and available seats
# -----------------------------------------

# Initialize counters
booked_seats = 0
available_seats = 0

# Check each seat in the list
for seat in seats:

    # If seat value is 1, it is booked
    if seat == 1:
        booked_seats += 1

    # Otherwise, it is available
    else:
        available_seats += 1

# Display the counts
print("Booked Seats =", booked_seats)
print("Available Seats =", available_seats)


# -----------------------------------------
# 2. Find the first available seat
# -----------------------------------------

# Loop through the list using index
for i in range(len(seats)):

    # Check if the seat is available
    if seats[i] == 0:

        # Seat numbers start from 1, so add 1 to index
        print("First Available Seat Number =", i + 1)

        # Stop searching after finding the first available seat
        break


# -----------------------------------------
# 3. Create a list of all available seats
# -----------------------------------------

# Empty list to store available seat numbers
available_seat_numbers = []

# Traverse the list
for i in range(len(seats)):

    # If seat is available
    if seats[i] == 0:

        # Store seat number (index + 1)
        available_seat_numbers.append(i + 1)

# Display all available seat numbers
print("Available Seat Numbers =", available_seat_numbers)


# -----------------------------------------
# 4. Check if bus is more than 70% occupied
# -----------------------------------------

# Total number of seats
total_seats = len(seats)

# Calculate occupancy percentage
occupancy_percentage = (booked_seats / total_seats) * 100

# Display occupancy percentage
print("Occupancy Percentage =", occupancy_percentage, "%")

# Check whether occupancy is greater than 70%
if occupancy_percentage > 70:
    print("Bus is more than 70% occupied")
else:
    print("Bus is not more than 70% occupied")
