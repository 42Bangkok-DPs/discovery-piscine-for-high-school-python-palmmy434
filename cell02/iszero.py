


number = input("Enter a number: ")

try:
    num = int(number)
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Please enter a valid integer.")
