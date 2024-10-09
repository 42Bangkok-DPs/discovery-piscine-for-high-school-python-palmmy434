

def main():
   
    user_input = input("Enter a number less than 25\n")
    
    try:
      
        number = int(user_input)


        if number > 25:
            print("Error")
        else:
         
            for i in range(number, 26):
                print(f"Inside the loop, my variable is {i}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
