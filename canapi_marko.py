grades = []  

while True:
    print("\n=== Grade Manager ===")
    print("1. Add Grade")
    print("2. Show Average Grade")
    print("3. List All Grades")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        grade = float(input("Enter a grade (0-100): "))
        if 0 <= grade <= 100:
            grades.append(grade)
            print("Grade added.")
        else:
            print("Invalid grade!")

    elif choice == '2':
        if grades:
            print(f"Average grade: {sum(grades) / len(grades):.2f}")
        else:
            print("No grades available.")

    elif choice == '3':
        print("Grades:", grades if grades else "No grades available.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
        