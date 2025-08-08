import time


def login_password():
    new_password = input("Please create your login password: ")
    return new_password


my_password = login_password()
print("Thank you, you have successfully created your password \n Now try to retype to enter the system")

correct_password = my_password
attempts = 0

while True:
    password = input("Enter you password: ")

    if password == correct_password:
        print("Login successful \n Now you can enter to the system")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

        if attempts == 5:
            print("Too many attempts. Please wait 15 seconds...")
            time.sleep(15)
            attempts = 0
