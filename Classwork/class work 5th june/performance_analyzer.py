# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# 1. Display all passed students (marks >= 40)
print("Passed Students Marks:")
for mark in marks:
    if mark >= 40:
        print(mark)

# 2. Count the number of failed students
failed_count = 0
for mark in marks:
    if mark < 40:
        failed_count += 1

print("Number of Failed Students:", failed_count)

# 3. Find highest and lowest marks without using max() or min()
highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# 4. Create a new list containing marks above 75
above_75 = []

for mark in marks:
    if mark > 75:
        above_75.append(mark)

print("Marks Above 75:", above_75)
