#!/usr/bin/env python3

def main():
    try:
        number = float(input("Enter a number: "))
        
        if number < 0:
            print("This number is negative.")
        elif number > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

