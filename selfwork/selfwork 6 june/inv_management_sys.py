'''
2. Inventory Management System 
Sample Data 
inventory = { 
    "Notebook": 45, 
    "Pen": 120, 
    "Pencil": 80, 
    "Eraser": 25, 
    "Marker": 15, 
    "Stapler": 8, 
    "Glue": 12, 
    "Scale": 30, 
    "Folder": 5, 
    "Calculator": 3 
} 
Tasks 
• Display products with stock less than 10.  
• Count products having stock more than 50.  
• Find the product with the minimum stock.  
• Create a list of products that require restocking (stock < 20).  
• Calculate the total inventory count. 
'''
# Dictionary containing product names and stock quantity

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Display products with stock < 10

print("Products with stock less than 10:")

for product in inventory:
    if inventory[product] < 10:
        print(product, ":", inventory[product])

# Count products having stock > 50

count = 0

for product in inventory:
    if inventory[product] > 50:
        count += 1

print("\nProducts having stock more than 50 =", count)

# Find product with minimum stock
min_product = min(inventory, key=inventory.get)

print("\nProduct with Minimum Stock:")
print(min_product, ":", inventory[min_product])

# Create list of products
# requiring restocking (stock < 20)
restock_list = []

for product in inventory:
    if inventory[product] < 20:
        restock_list.append(product)

print("\nProducts Requiring Restocking:")
print(restock_list)

# Calculate total inventory count
total_stock = 0

for product in inventory:
    total_stock += inventory[product]

print("\nTotal Inventory Count =", total_stock)
