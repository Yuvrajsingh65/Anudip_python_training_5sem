'''
9. Warehouse Product Inspection 
Problem Statement 
Product IDs and quality status: 
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 
Write a program to: 
• Display failed product IDs.  
• Count passed and failed products.  
• Calculate pass percentage.  
• Stop checking if 3 failures are found. 
'''
# Product ID and Quality Status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# Variables to count pass and fail products
pass_count = 0
fail_count = 0

print("Failed Product IDs:")

# Check each product
for pid, status in products:

    # If product passed
    if status == "Pass":
        pass_count += 1

    # If product failed
    else:
        fail_count += 1
        print(pid)

        # Stop checking if 3 failures are found
        if fail_count == 3:
            print("3 failures found. Stopping inspection.")
            break

# Display Pass and Fail Counts
print("\nPassed Products =", pass_count)
print("Failed Products =", fail_count)

# Calculate Pass Percentage

total_products = pass_count + fail_count

pass_percentage = (pass_count / total_products) * 100

print("Pass Percentage =", pass_percentage, "%")
    
