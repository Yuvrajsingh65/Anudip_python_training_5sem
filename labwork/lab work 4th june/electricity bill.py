# Program: Electricity Bill Calculator
# Task: Calculate bill based on slab rates

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = (100 * 1) + (units - 100) * 2
else:
    bill = (100 * 1) + (100 * 2) + (units - 200) * 3

# Categorize consumption
if units <= 100:
    category = "Low Consumption"
elif units <= 200:
    category = "Medium Consumption"
else:
    category = "High Consumption"

print(f"Units Consumed: {units}")
print(f"Total Bill: ₹{bill}")
print(f"Category: {category}")
