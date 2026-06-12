'''
Problem 8: City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored below. 
Sample Data 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities with temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (<35°C). 
'''
# City Temperature Monitoring System

# Dictionary storing city names and their temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# Task 1: Display cities with temperature above 40°C
print("Cities with Temperature Above 40°C:")

for city in temperature:
    if temperature[city] > 40:
        print(city, ":", temperature[city])

# Task 2: Find the hottest city
hottest_city = max(temperature, key=temperature.get)

print("\nHottest City:")
print(hottest_city, ":", temperature[hottest_city])

# Task 3: Find the coolest city
coolest_city = min(temperature, key=temperature.get)

print("\nCoolest City:")
print(coolest_city, ":", temperature[coolest_city])

# Task 4: Calculate average temperature
average_temp = sum(temperature.values()) / len(temperature)

print("\nAverage Temperature:", average_temp)

# Task 5: Create a list of pleasant cities
# Pleasant cities are those with temperature less than 35°C
pleasant_cities = []

for city in temperature:
    if temperature[city] < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities (<35°C):")
print(pleasant_cities)
