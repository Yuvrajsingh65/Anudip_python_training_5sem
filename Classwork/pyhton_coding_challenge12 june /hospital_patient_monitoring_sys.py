'''
Problem 9: Hospital Patient Monitoring System 
Problem Statement 
Patient heart rates are recorded below. 
Sample Data 
heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
} 
Tasks 
1. Display critical patients (heart rate >100).  
2. Find highest and lowest heart rate.  
3. Calculate average heart rate.  
4. Count stable patients (60–100 bpm). 
'''
# Hospital Patient Monitoring System

# Dictionary storing patient ID and heart rate
heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# Task 1: Display critical patients
# Critical patients have heart rate greater than 100 bpm
print("Critical Patients:")

for patient in heart_rate:
    if heart_rate[patient] > 100:
        print(patient, ":", heart_rate[patient])

# Task 2: Find highest heart rate
highest = max(heart_rate.values())

# Find lowest heart rate
lowest = min(heart_rate.values())

print("\nHighest Heart Rate:", highest)
print("Lowest Heart Rate:", lowest)

# Task 3: Calculate average heart rate
average = sum(heart_rate.values()) / len(heart_rate)

print("\nAverage Heart Rate:", average)

# Task 4: Count stable patients
# Stable patients have heart rate between 60 and 100 bpm
count = 0

for rate in heart_rate.values():
    if rate >= 60 and rate <= 100:
        count = count + 1

print("\nNumber of Stable Patients:", count)
