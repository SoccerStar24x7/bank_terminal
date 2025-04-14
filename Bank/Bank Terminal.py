import json

database = "Bank/Info.json"


def account(username, password):
    with open(database, "r") as f:
        logins = json.load(f)

    balance = float(logins[username]["balance"])

    print()
    take = int(input(f"Hello {username}! You currently have ${balance} in your bank account. Type '1' if you are withdrawing, and '2' if you are depositing. "))
    if take == 1:
        amount = float(input("How much are you withdrawing? "))
        balance -= amount

    elif take == 2:
        amount = float(input("How much are you depositing? "))
        balance += amount

    else:
        print("what")
        exit()

    logins[username]["balance"] = balance

    with open(database, "w") as h:
        json.dump(logins, h)
    print(f"Your balance is now ${balance}.")
    exit(0)


def create(logins):

    username = input("What do you want your username to be? ")  # asks the user what they want their username to be
    print()
    pass1 = input("What do you want your password to be? ")  # asks the user what they want their password to be
    pass2 = input("Please input your password again to verify: ")  # asks the user to type the password again to verify
    print()

    if pass1 == pass2:  # if both passwords match up...

        balance = float(input("What is your balance in your bank account? "))

        logins[username] = {"password": pass1, "balance": balance}

        with open(database, "w") as f:  # opens Database.json in write mode as "f"
            json.dump(logins, f)  # dumps logins into the Database

        print("Your account has been successfully made! Please rerun this program and type in your new login information. ")  # tells the user that the account has been successfully made and to rerun this program
        exit(0)  # stops the program

    else:
        print("Passwords do not match.")  # tells the user that the password do not match
        exit(0)  # stops the program


def main():

    count = 0  # creates a variable as "count" that counts how many times the user gets a login wrong
    while count <= 5:  # creates a while loop that runs while count is less than 5. This is to prevent hackers trying to brute force their way into the system

        with open(database, "r") as f:  # opens Database.json in read mode as "f"
            logins = json.load(f)  # saves whatever is on f as "logins"

        print()  # prints a blank line to keep fresh

        print("Welcome to the Login Terminal! ")  # prints the welcome page for the login terminal

        print()  # prints a blank line to keep fresh

        username = input("What is your username? ")  # gets input from the user about which username they want to enter

        if username in logins.keys():  # if the username is one of the keys in logins...
            password = input("What is the password? ")  # asks them for the corresponding password (value) for that account
            passwords = logins[username]["password"]
            if password in passwords:  # if the password is the correct value for that item...
                account(username, password)

            else:  # else:
                print("Password incorrect. ")  # prints that the password in incorrect

                make = input("Would you like to create an account (y/n)? ")  # asks the user if they want to create an account

                if make == "y":  # if they do...
                    create(logins)  # runs the function "create"
                else:  # else:
                    exit()

        else:  # else:
            print("Username invalid. ")  # prints that the username is invalid

            make = input("Would you like to create an account (y/n)? ")  # asks the user if they want to create an account

            if make == "y":  # if they do...
                create(logins)  # runs the function "create"
            else:  # else:
                exit(0)


main()
