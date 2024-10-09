#!/usr/bin/env python3

def main():
    # Prompt the user for input
    user_input = input("Enter a number\n")
    
    try:
        # Convert input to an integer
        number = int(user_input)

        # Generate and display the multiplication table
        for i in range(10):
            print(f"{i} x {number} = {i * number}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

