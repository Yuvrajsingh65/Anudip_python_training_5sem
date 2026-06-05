#write a prograamm to check that three side of triangle is form or not 
# Input three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check triangle condition
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")
