# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# Display the original list
print("Numbers List:", numbers)

# Print heading for consecutive pairs
print("\nConsecutive Number Pairs:")

# Traverse the list from the first element to the second-last element
for i in range(len(numbers) - 1):

    # Check if the next number is exactly 1 greater
    # than the current number
    if numbers[i] + 1 == numbers[i + 1]:

        # If yes, print the consecutive pair
        print(numbers[i], numbers[i + 1])
