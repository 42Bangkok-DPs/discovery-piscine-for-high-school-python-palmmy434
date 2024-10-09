#!/usr/bin/env python3

def main():
    # Ask the user for their age
    age_input = input("Please tell me your age: ")
    
    # Convert the input to an integer
    age = int(age_input)

    # Display the current age and future ages
    print(f"You are currently {age} years old.")
    print(f"In 10 years, you'll be {age + 10} years old.")
    print(f"In 20 years, you'll be {age + 20} years old.")
    print(f"In 30 years, you'll be {age + 30} years old.")

if __name__ == "__main__":
    main()
