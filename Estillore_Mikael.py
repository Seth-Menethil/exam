import math

while True:
    try:
        print("TRIGONOMETRIC CALCULATOR")
        print("1) Sine")
        print("2) Cosine")
        print("3) Tangent")
        print("4) Exit.")
        choice = int(input("Choose an option (1-4): "))
        angle = int(input("Enter angle value: "))
        while True:
            try:
                if choice == 1:
                    input("Enter angle value: ")
                    value = input("Is this value in (d) degrees or (r)adians? : ")
            except ValueError:
             print("Invalid input!")
    except ValueError:
        print("Invalid input!")