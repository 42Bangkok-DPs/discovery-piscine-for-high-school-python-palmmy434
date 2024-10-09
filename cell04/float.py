#!/usr/bin/env python3

def main():
    # Ask the user for a number
    number_input = input("Give me a number: ")

    # Try to convert the input to a float
    try:
        number = float(number_input)
        
        # Check if the number is an integer
        if number.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()
