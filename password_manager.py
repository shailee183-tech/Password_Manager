import random
import string

passwords = {}

#load existing passwords from file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@$$%&"
    password = ''.join(random.choice(chars) for _ in range(8))
    return password

while True :
    print("\n---------------PERSONAL PASSWORD MANAGER---------------")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter the website: ")
        pwd = input("Enter the password: ")

        passwords[site] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Password saved successfully!")

    elif choice == "2":
        if not passwords:
            print("No passwords saved.")
        else:
            print("\nSaved Passwords:")
            for site, pwd in passwords.items():
                print(f"{site}: {pwd}")

    elif choice == "3":
        new_password = generate_password()
        print(f"Generated Password: {new_password}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")