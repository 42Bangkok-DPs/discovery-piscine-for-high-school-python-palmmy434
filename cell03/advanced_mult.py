#!/usr/bin/env python3

def main():
    # Start from the first multiplication table
    i = 0

    # Outer loop for each multiplication table
    while i <= 10:
        print(f"Table de {i}:", end=" ")

        # Inner loop for multiplication values
        j = 0
        while j <= 10:
            print(i * j, end=" ")
            j += 1
            
        print()  # Move to the next line
        i += 1

if __name__ == "__main__":
    main()
