#!/usr/bin/env python3
import math

def main():
    # Ask the user for a number
    number_input = input("Give me a number: ")

    # Try to convert the input to a float
    try:
        number = float(number_input)
        
        # Round up the number
        rounded_number = math.ceil(number)
        
        # Display the rounded number
        print(rounded_number)
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()
