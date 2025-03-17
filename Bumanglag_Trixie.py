while True:
    print("\n===== Factorial and Summation Menu =====")
    print("1. Compute factorial")
    print("2. Compute summation (1 to n)")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer!")
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print(f"Factorial of {n} is {fact}")

    elif choice == '2':
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer!")
        else:
            total = n * (n + 1) // 2
            print(f"Sum of numbers from 1 to {n} is {total}")

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-3")


