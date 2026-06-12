'''
Problem 3: Food Delivery Performance Dashboard 
Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes) 
'''
# Food Delivery Performance Dashboard

# List containing delivery times of orders (in minutes)
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Find the fastest delivery time
# min() returns the smallest value in the list
print("Fastest Delivery Time =", min(delivery_times), "minutes")

# 2. Find the slowest delivery time
# max() returns the largest value in the list
print("Slowest Delivery Time =", max(delivery_times), "minutes")

# 3. Calculate the average delivery time
average = sum(delivery_times) / len(delivery_times)

print("Average Delivery Time =", average, "minutes")

# 4. Display delayed orders (more than 45 minutes)
print("\nDelayed Orders:")

for time in delivery_times:
    if time > 45:
        print(time, "minutes")

# 5. Categorize deliveries into Fast, Normal and Delayed

# Empty lists to store delivery times
fast = []
normal = []
delayed = []

# Check each delivery time
for time in delivery_times:

    # Fast delivery: 30 minutes or less
    if time <= 30:
        fast.append(time)

    # Normal delivery: between 31 and 45 minutes
    elif time <= 45:
        normal.append(time)

    # Delayed delivery: more than 45 minutes
    else:
        delayed.append(time)

# Display all categories
print("\nFast Deliveries (<=30 minutes):")
print(fast)

print("\nNormal Deliveries (31-45 minutes):")
print(normal)

print("\nDelayed Deliveries (>45 minutes):")
print(delayed)
