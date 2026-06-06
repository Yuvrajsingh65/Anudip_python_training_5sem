'''
1. E-Commerce Order Analysis 
Problem Statement 
An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. 
'''
# E-Commerce Order Analysis

# Create a list of orders.
# Each order is stored as a tuple:
# (Product Name, Product Price)

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display all products costing more than ₹1000
print("Products costing more than ₹1000:")

# Go through each product in the list
for product, price in orders:
    
    # Check if the product price is greater than 1000
    if price > 1000:
        
        # Display product name and price
        print(product, "=", price)

# 2. Find the most expensive product

# Assume the first product is the most expensive
most_expensive_product = orders[0][0]
highest_price = orders[0][1]

# Compare every product price with highest_price
for product, price in orders:
    
    # If current product price is greater
    if price > highest_price:
        
        # Update highest price
        highest_price = price
        
        # Update product name
        most_expensive_product = product

print("\nMost Expensive Product:")
print(most_expensive_product, "=", highest_price)

# 3. Calculate total order value
# Variable to store total price of all products
total_value = 0

# Add the price of each product to total_value
for product, price in orders:
    total_value = total_value + price

print("\nTotal Order Value = ₹", total_value)

# 4. Count products costing below ₹1000

# Variable to count products
count = 0

# Check every product price
for product, price in orders:
    
    # If price is less than 1000
    if price < 1000:
        
        # Increase count by 1
        count = count + 1

print("\nNumber of products costing below ₹1000 =", count)
