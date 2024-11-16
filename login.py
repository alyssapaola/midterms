users = []
password = []

print("\nSimple Login System")

while True:
    print("\nMain Menu")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == '1':
        print("\n--- Register ---")
        while True:
            username = input("Enter a username (or type 'exit' to cancel): ")
            password = input("Enter a password: ")
            confirm_password = input("Confirm your password: ")

            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue

            for user in users:
                if user["username"] == username:
                    print("Username already exists. Please choose a different username.")
                    break
            else:
                users.append(username)
                print("Registration successful! You can now log in.")
                break

            choice = input("Do you want to try registering again? (yes/no): ")
            if choice.lower() != 'yes':
                print("Returning to the main menu.")
                break                         
            elif choice == '2':
                print("\n--- Login ---")
                while True:
                    username = input("Enter your username (or type 'exit' to cancel): ")
                    if username.lower() == 'exit':
                        print("Login canceled. Returning to the main menu.")
                        break
                    password = input("Enter your password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Welcome, {username}! Login successful.")

                while True:
                    print(f"Logged in as {username}.")
                    logout = input("Type 'logout' to exit or 'continue' to stay logged in: ")
                    if logout.lower() == 'logout':
                        print("You have logged out. Returning to the main menu.")
                        break
                    elif logout.lower() != 'continue':
                        print("Invalid option. Please type 'logout' or 'continue'.")
                break
        else:
            print("Invalid username or password. Please try again.")

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
else:
    print("Invalid option. Please select a valid option (1-3).")
