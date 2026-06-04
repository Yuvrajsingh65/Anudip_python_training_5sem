name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

if net > 50000:
    grade = "Senior Grade"
elif net > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

print("\nEmployee:", name)
print("Gross Salary:", gross)
print("Net Salary:", net)
print("Grade:", grade)
