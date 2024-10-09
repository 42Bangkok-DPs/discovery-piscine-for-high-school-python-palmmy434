
def main():
 
    number_input = input("Give me a number: ")

   
    try:
        number = float(number_input)
        
        if number.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()
