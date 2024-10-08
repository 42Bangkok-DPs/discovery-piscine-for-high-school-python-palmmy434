#!/usr/bin/env python3

# Prompt the user for a number
number = input("Enter a number: ")

# Check if the input can be converted to an integer
try:
    num = int(number)
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Please enter a valid integer.")
