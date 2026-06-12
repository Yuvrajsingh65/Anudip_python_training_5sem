Problem 4: Online Shopping Inventory System 
Problem Statement 
An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units). 
'''
# Online Shopping Inventory System

# Dictionary storing product names and stock quantities
inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products having stock less than 15 units
print("Products with stock below 15 units:")

for product in inventory:
    if inventory[product] < 15:
        print(product, "=", inventory[product])

# 2. Find the product with maximum stock
highest = max(inventory, key=inventory.get)

print("\nProduct with Maximum Stock:")
print(highest, "=", inventory[highest])

# 3. Find the product with minimum stock
lowest = min(inventory, key=inventory.get)

print("\nProduct with Minimum Stock:")
print(lowest, "=", inventory[lowest])

# 4. Calculate the total stock available
total = sum(inventory.values())

print("\nTotal Stock Available =", total)

# 5. Create a list of products that need restocking
# Restocking is needed when stock is less than 10

restock_list = []

for product in inventory:
    if inventory[product] < 10:
        restock_list.append(product)

print("\nProducts Requiring Restocking:")
print(restock_list)
