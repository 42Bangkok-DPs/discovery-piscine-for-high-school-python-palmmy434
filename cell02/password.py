

def main():
    password = "Python is awesome"
    entered_password = input("Enter the password: ")

    if entered_password == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()
