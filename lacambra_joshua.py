while True: 
    print("\n=== BMI CALCULATOR ===")
    print("1. Calculate BMI(Metric)")
    print("2. Calculate BMI(Imperial)")
    print("3.Exit")
    break

choice = input ("Enter your choice: ")

if choice == "1":
    weight = float(input("Enter Weight in kg: "))
    height = float(input("Enter Height in meters: "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

elif choice == "2":
    weight = float(input("Enter Weight in pounds: "))
    height = float(input("Enter Height in inches: "))
    bmi = (703 * weight) / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

elif choice == "3":
    print("Exiting BMI Calculator. Goodbye!")
    
else:
    print("Invalid Choice. Please Enter 1, 2, 3.")
    