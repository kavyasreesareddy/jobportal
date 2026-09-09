
import json

# Project name: Student Management System

def register():
    n = input("Enter name: ")
    e = input("Enter email: ")
    p = input("Enter password: ")
    c_p = input("Enter confirm password: ")

    # Check password
    if p != c_p:
        print("Password and confirm password do not match")
        return

    new_reg_user_data = {
        "name": n,
        "email": e,
        "password": p
    }

    # Read existing users
    try:
        with open("reg_user_data.json", "r") as r_file:
            users = json.load(r_file)

    except FileNotFoundError:
        users = []

    # Add new user
    users.append(new_reg_user_data)

    # Save users
    with open("reg_user_data.json", "w") as w_file:
        json.dump(users, w_file, indent=4)

    print("User added successfully!")


def login():
    e = input("Enter email: ")
    p = input("Enter password: ")

    try:
        with open("reg_user_data.json", "r") as r_file:
            users = json.load(r_file)

    except FileNotFoundError:
        print("No registered users found.")
        return

    for user in users:
        if user["email"] == e and user["password"] == p:
            print("Login successful!")
            print("Welcome", user["name"])
            return

    print("Invalid email or password")


def logout():
    print("Logged out successfully!")


# Main menu
while True:
    print("\n----- Student Management System -----")
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Exit")

    i = int(input("Choose an option: "))

    if i == 1:
        register()

    elif i == 2:
        login()

    elif i == 3:
        logout()

    elif i == 4:
        print("Thank you!")
        break

    else:
        print("Invalid option")