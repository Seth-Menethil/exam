import math
pi = math.pi
while True:
    try:
        print("\nTRIGONOMETRIC CALCULATOR")
        print("1) Sine")
        print("2) Cosine")
        print("3) Tangent")
        print("4) Exit.")
        choice = int(input("Choose an option (1-4): "))
        while True:
                if choice == 4:
                    print("Exiting program.")
                break
        angle = int(input("Enter angle value in Degrees: "))
        radians = math.radians(angle)  
        if choice == 1:
            result = math.sin(radians)
            print(f"Sine({angle}°) = {result}")
            break
        elif choice == 2:
            result = math.cos(radians)
            print(f"Cosine({angle}°) = {result}")
            break
        elif choice == 3:
            result = math.tan(radians)
            print(f"Tangent({angle}°) = {result}")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input!")

