#!/usr/bin/env python3

def main():
    # Prompt the user for two numbers
    first_number = float(input("Enter the first number:\n"))
    second_number = float(input("Enter the second number:\n"))
    
    # Calculate the multiplication
    result = first_number * second_number
    
    # Display the result of the multiplication
    print(f"{first_number} x {second_number} = {result}")
    
    # Determine if the result is positive, negative, or zero
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")

if __name__ == "__main__":
    main()
