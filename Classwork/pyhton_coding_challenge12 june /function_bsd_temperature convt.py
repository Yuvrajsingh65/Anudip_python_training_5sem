'''
Problem 15: Function-Based Temperature Converter 
Problem Statement 
Daily temperatures recorded in Celsius are given below. 
Sample Data 
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
Tasks 
Create functions to: 
1. Convert Celsius to Fahrenheit.  
2. Display all temperatures in Fahrenheit.  
3. Find the highest Fahrenheit temperature.  
4. Find the lowest Fahrenheit temperature.  
5. Calculate the average Fahrenheit temperature. 
'''
# Function-Based Temperature Converter

# List storing temperatures in Celsius
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to display all temperatures in Fahrenheit
def display_fahrenheit():
    print("Temperatures in Fahrenheit:")
    
    for temp in temperatures:
        print(celsius_to_fahrenheit(temp))

# Function to find the highest Fahrenheit temperature
def highest_fahrenheit():
    fahrenheit_list = []

    for temp in temperatures:
        fahrenheit_list.append(celsius_to_fahrenheit(temp))

    print("Highest Fahrenheit Temperature =", max(fahrenheit_list))

# Function to find the lowest Fahrenheit temperature
def lowest_fahrenheit():
    fahrenheit_list = []

    for temp in temperatures:
        fahrenheit_list.append(celsius_to_fahrenheit(temp))

    print("Lowest Fahrenheit Temperature =", min(fahrenheit_list))

# Function to calculate average Fahrenheit temperature
def average_fahrenheit():
    fahrenheit_list = []

    for temp in temperatures:
        fahrenheit_list.append(celsius_to_fahrenheit(temp))

    average = sum(fahrenheit_list) / len(fahrenheit_list)

    print("Average Fahrenheit Temperature =", average)

# Function Calls
display_fahrenheit()
highest_fahrenheit()
lowest_fahrenheit()
average_fahrenheit()
