balance = 0
while True:
    
    print("\n=== ATM MACHINE ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Exit")
    option = int(input("Select an option (1 - 4): "))

    if option == 1:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        if amount < 1:
            print ("Cannot Deposit this Amount!")
        else:
            print(f"Deposited {amount}. Your new balance is {balance}")
        
    elif option == 2:
        amount = int(input("Enter withdrawal amount: "))
        if amount < balance:
            print("Invalid Input!")
        else:
            balance -= amount
            print(f"Withdrew {amount}. Your new balance is {balance}")

    elif option == 3:
        print(f"Your current balance is {balance}")

    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option (1 - 4).")