
import math

def main():
    
    number_input = input("Give me a number: ")


    try:
        number = float(number_input)
        
      
        rounded_number = math.ceil(number)
    
        print(rounded_number)
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()
