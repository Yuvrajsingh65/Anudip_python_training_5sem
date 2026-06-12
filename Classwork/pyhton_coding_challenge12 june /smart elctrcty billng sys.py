'''
Problem 1: Smart Electricity Billing System 
Problem Statement
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200-400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300). 
'''
 # Smart Electricity Billing System

# Dictionary storing house number as key
# and electricity units consumed as value
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses consuming more than 400 units:")
for house in units:
    if units[house] > 400:
        print(house, "=", units[house])

# 2. Find the highest-consuming house
highest_house = max(units, key=units.get)

print("\nHighest Consuming House:")
print(highest_house, "=", units[highest_house])

# 3. Find the lowest-consuming house
lowest_house = min(units, key=units.get)

print("\nLowest Consuming House:")
print(lowest_house, "=", units[lowest_house])

# 4. Calculate total units consumed
total = sum(units.values())

print("\nTotal Units Consumed =", total)

# 5. Create separate lists for low, medium and high consumption

# Empty lists to store house names
low = []
medium = []
high = []

# Check each house and put it in the correct list
for house in units:

    # Less than 200 units
    if units[house] < 200:
        low.append(house)

    # Between 200 and 400 units
    elif units[house] <= 400:
        medium.append(house)

    # More than 400 units
    else:
        high.append(house)

print("\nLow Consumption Houses (<200 units):")
print(low)

print("\nMedium Consumption Houses (200-400 units):")
print(medium)

print("\nHigh Consumption Houses (>400 units):")
print(high)

# 6. Count houses eligible for energy-saving campaign
# Houses with consumption greater than 300 units

count = 0

for house in units:
    if units[house] > 300:
        count = count + 1

print("\nNumber of houses eligible for Energy-Saving Campaign =", count)
