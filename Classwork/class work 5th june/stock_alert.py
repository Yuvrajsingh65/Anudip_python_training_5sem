# List containing stock quantity of products
# Each position in the list represents a product
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# -----------------------------------------
# 1. Display Products that are Out of Stock
# -----------------------------------------

print("Products that are Out of Stock:")

# Check every product in the list
for i in range(len(stock)):

    # If stock quantity is 0, product is out of stock
    if stock[i] == 0:

        # Product number starts from 1
        print("Product", i + 1)


# -----------------------------------------
# 2. Display Products that Need Restocking
#    (Quantity less than 10)
# -----------------------------------------

print("\nProducts that Need Restocking:")

# Traverse the stock list
for i in range(len(stock)):

    # Check if quantity is less than 10
    if stock[i] < 10:

        # Display product number and quantity
        print("Product", i + 1, "- Stock =", stock[i])


# -----------------------------------------
# 3. Count Available Products
# -----------------------------------------

# Variable to count available products
available_products = 0

# Check every product
for quantity in stock:

    # Product is available if quantity is greater than 0
    if quantity > 0:
        available_products += 1

# Display total available products
print("\nAvailable Products =", available_products)


# -----------------------------------------
# 4. Create a New List of Products
#    Having Stock >= 15
# -----------------------------------------

# Empty list to store products with stock >= 15
high_stock_products = []

# Traverse the stock list
for quantity in stock:

    # Check if stock is 15 or more
    if quantity >= 15:

        # Add quantity to new list
        high_stock_products.append(quantity)

# Display the new list
print("Products with Stock >= 15 =", high_stock_products)
