while True:
    print("\n======== Multiplication Table Menu =======")
    print("1. Generate a Multiplication Table")
    print("2. Exit")
 
    choice = input("Choose an option (1-2): ")
 
    if choice == "1":
        num = int(input("\nEnter an integer: "))
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    elif choice == "2":
        print("\nExiting Multiplication Table Program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter 1 or 2.")