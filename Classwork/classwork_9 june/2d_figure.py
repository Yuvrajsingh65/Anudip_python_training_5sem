#create a python program which provides a menu to the user to select the 2 dimensional figure(circle, rectangle, square) after selecting the user
# again ask to select a operatiom provide the input of corresponding data for the figure after input of corresponding data again provide a
# menu to select the operation area,perimeter and as per the data provided by user display the result f operation. this task will be repeated
# again and again until user select the option to exit from that figure.
import math
def area_circle(radius):
    return math.pi * radius ** 2
def perimeter_circle(radius):
    return 2 * math.pi * radius
def area_rectangle(length, width):
    return length * width
def perimeter_rectangle(length, width):
    return 2 * (length + width)
def area_square(side):
    return side ** 2
def perimeter_square(side):
    return 4 * side
def main():
    while True:
        print("Select a 2D figure:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            while True:
                print("Select an operation:")
                print("1. Area")
                print("2. Perimeter")
                print("3. Back to main menu")
                operation = input("Enter your choice (1-3): ")
                if operation == '1':
                    print(f"Area of the circle: {area_circle(radius):.2f}")
                elif operation == '2':
                    print(f"Perimeter of the circle: {perimeter_circle(radius):.2f}")
                elif operation == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            while True:
                print("Select an operation:")
                print("1. Area")
                print("2. Perimeter")
                print("3. Back to main menu")
                operation = input("Enter your choice (1-3): ")
                if operation == '1':
                    print(f"Area of the rectangle: {area_rectangle(length, width):.2f}")
                elif operation == '2':
                    print(f"Perimeter of the rectangle: {perimeter_rectangle(length, width):.2f}")
                elif operation == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            side = float(input("Enter the side length of the square: "))
            while True:
                print("Select an operation:")
                print("1. Area")
                print("2. Perimeter")
                print("3. Back to main menu")
                operation = input("Enter your choice (1-3): ")
                if operation == '1':
                    print(f"Area of the square: {area_square(side):.2f}")
                elif operation == '2':
                    print(f"Perimeter of the square: {perimeter_square(side):.2f}")
                elif operation == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    
