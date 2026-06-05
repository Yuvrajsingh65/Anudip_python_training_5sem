marks = []
fail_count = 0

for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)
    if m < 40:
        fail_count += 1

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Subjects Failed:", fail_count)
