#!/usr/bin/env python3

def main():
    # Ask the user for two numbers
    first_number_input = input("Give me the first number: ")
    second_number_input = input("Give me the second number: ")

    # Convert the inputs to float for accurate calculations
    first_number = float(first_number_input)
    second_number = float(second_number_input)

    print("Thank you!")

    # Perform and display the calculations
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    print(f"{first_number} / {second_number} = {first_number / second_number}")
    print(f"{first_number} * {second_number} = {first_number * second_number}")

if __name__ == "__main__":
    main()
