'''
9. Warehouse Product Inspection 
Problem Statement 
Product IDs and quality status: 
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"),
'''
# Product ID and Quality Status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail")
]

# Count Passed and Failed Products

pass_count = 0
fail_count = 0

# Check each product
for pid, status in products:

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("Passed Products =", pass_count)
print("Failed Products =", fail_count)

# Display Failed Product IDs

print("\nFailed Product IDs:")

for pid, status in products:

    if status == "Fail":
        print(pid)

# Calculate Pass Percentage

total_products = len(products)

pass_percentage = (pass_count / total_products) * 100

print("\nPass Percentage =", pass_percentage, "%")

# Determine Overall Result
if pass_percentage >= 50:
    print("Overall Result : ACCEPTED")
else:
    print("Overall Result : REJECTED")
