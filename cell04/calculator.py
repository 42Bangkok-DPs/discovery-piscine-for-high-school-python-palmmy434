

def main():

    first_number_input = input("Give me the first number: ")
    second_number_input = input("Give me the second number: ")

    
    first_number = float(first_number_input)
    second_number = float(second_number_input)

    print("Thank you!")

    
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    print(f"{first_number} / {second_number} = {first_number / second_number}")
    print(f"{first_number} * {second_number} = {first_number * second_number}")

if __name__ == "__main__":
    main()
