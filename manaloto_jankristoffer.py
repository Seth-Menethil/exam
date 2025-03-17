num_choice = 0
num_guess = 0
num_true = 5

print("=== Number Guessing Game ===")
print("1. Start/Restart Game")
print("2. Exit")

while num_choice != 2:
    num_choice = int(input("Choose an option (1-2): "))
    if num_choice == 2:
        print("Exiting the Number Guessing Game. Goodbye!")
        break
    
    while num_guess != -1 or num_guess != num_true:
        num_guess = int(input("Guess the secret number (or -1 to quit): "))

        if num_guess == -1:
            print("Restart? (1-2)")
            break
        elif num_guess < num_true:
            print("Too low")
        elif num_guess > num_true:
            print("Too High")
        elif num_guess == num_true:
            print("Correct!")
            break