#!/usr/bin/env python3

def main():
    while True:
        # Prompt the user for input
        user_input = input("What you gotta say? : ")
        
        # Check if the input is "STOP"
        if user_input.upper() == "STOP":
            break
        
        # Respond to the input
        print("I got that! Anything else? : ")

if __name__ == "__main__":
    main()
