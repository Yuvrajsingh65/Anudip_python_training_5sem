'''
Smart Parking System 
Problem Statement 
Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots. 
'''
# List representing parking slots
# 1 = Occupied slot
# 0 = Available slot

slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Variable to count occupied slots
occupied = 0

# Variable to count available slots
available = 0

# Check each slot in the list
for slot in slots:

    # If slot value is 1, it is occupied
    if slot == 1:
        occupied = occupied + 1

    # If slot value is 0, it is available
    else:
        available = available + 1

# Display the results
print("Occupied Slots =", occupied)
print("Available Slots =", available)
