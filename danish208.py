#Name: Danish Al-Harroz Bin Mohd Shafirul 
#Class: KCDIM1443E
#Matrics Number: 2023509613
#Topic: Individual Project Expenses Tracker System

print("Welcome to the expense tracker system")
welcome = input("Have you registered before? (yes/no): ")

if welcome == "no":
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        password1 = input("Confirm password: ")
        
        if password == password1:
            try:
                # Attempt to open the file in 'x' mode to create a new file
                with open(username+".txt", "x") as file:
                    file.write(username + ":" + password)
                print("Registration successful!")
                welcome = "yes"  # Automatically log in the user after registration
                break
            except FileExistsError:
                print("Username already exists. Please choose another one.")
        else:
            print("Passwords do not match!")

if welcome == "yes":
    while True:
        login1 = input("Enter your username: ")
        login2 = input("Enter your password: ")
        
        try:
            with open(login1+".txt", "r") as file:
                data = file.read().strip()  # Read the content and strip whitespace
            
            if data == login1 + ":" + login2:
                print("Login successful! Welcome,", login1)
                break
            else:
                print("Incorrect username or password.")
        except FileNotFoundError:
            print("User not found. Please register first.")
            welcome = "no"
            break
        
expenses = {
    'Food': 0,
    'Transportation': 0,
    'Entertainment': 0
}

def display_expenses():
    """Display current expenses in each category."""
    print("\nCurrent Expenses:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print()

def add_expense():
    """Add an expense to a specific category."""
    category = input("Enter the category (Food, Transportation, Entertainment): ").capitalize()
    if category in expenses:
        try:
            amount = float(input(f"Enter the expense amount for {category}: $"))
            expenses[category] += amount
            print(f"Added ${amount:.2f} to {category}.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    else:
        print("Invalid category. Please choose from Food, Transportation, or Entertainment.")

def view_total_expenses():
    """View the total expenses across all categories."""
    total = sum(expenses.values())
    print(f"\nTotal Expenses: ${total:.2f}\n")

def expense_tracker():
    """Main loop for the Expense Tracker."""
    while True:
        print("\nExpense Tracker Menu:")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            display_expenses()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_total_expenses()
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from 1, 2, 3, or 4.")

# Run the Expense Tracker
expense_tracker()


