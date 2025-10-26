welcome_message = print("Welcome to the Personal Finance Tracker!")

expenses = {}
#Function to display the menu and handle decision making from the user.
def display_menu():
    #Keep showing the menu to the user until they decide to exit by pressing option 4
    while True:
        print("----------------------------------------------------------------")
        print("What would you like to do? \n1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit")
        user_input = input("Choose an option: ")
        print("----------------------------------------------------------------")

        if user_input == "1":
            add_expense(expenses)
        elif user_input == "2":
            view_expenses(expenses)
        elif user_input == "3":
            view_summary(expenses)
        elif user_input == "4":
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid option. Please choose a valid option.")


#Function to add expenses
def add_expense(expenses):
    while True:
        try:
            expense_description = input("Enter expense description: ")
            expense_category = input("Enter category: ")
            expense_amount = float(input("Enter amount: "))
            expense = (expense_description,expense_amount)

            if expense_category in expenses:
                expenses[expense_category].append(expense)
            else:
                expenses[expense_category] = [expense]
            
            print("Expense added successfully!")
            print("----------------------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
        
        cont = input("Do you want to add another expense? (yes/no): ")
        if cont.lower() != "yes":
            break


#Function to view all expenses
def view_expenses(expenses):
    #Iterate through each category to view each detailed expense
    for category, expense_list in expenses.items():
        print(f"Category: {category}")
        for description, amount in expense_list:
            print(f"\t- {description}: ${amount}")


#Function to view a summary of all the 
def view_summary(expenses):
    print("Summary: ")
    overall_total = 0
    #Iterate through each category to get  the total amount spent in each category
    for category, expense_list in expenses.items():
        total_category = 0

        for description,amount in expense_list:
            total_category += amount
            overall_total += amount
        print(f"{category}: ${total_category:.2f}")
    
    #Ask user if they want to view the overall total
    user_input = input("Would you like me to calculate the total amount spent? (yes/no) ")
    if user_input.lower() == "yes":
        print(f"Total amount spent: ${overall_total:.2f}")
    else:
        pass


display_menu()