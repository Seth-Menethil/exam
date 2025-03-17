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
        angle = float(input("Enter angle value: "))
        while True:
            try:
                if choice == 1:
                    value = input("Is this value in (d) degrees or (r)adians? : ")
                    options = ["d", "D", "r", "R"]
                    if value in options and value == "d" or value == "D":    
                        degree = angle * pi / 180
                        print(f"Sine ({angle}\u00B0) = {degree}")
                        break
                    elif value in options and value == "r" or value == "R":
                        radians = degree * (pi/180)
                        print(f"Sine ({angle}rad) = {radians}")
                        break
                if choice == 2:
                    value = input("Is this value in (d) degrees or (r)adians? : ")
                    options = ["d", "D", "r", "R"]
                    if value in options and value == "d" or value == "D":    
                        degree = angle * pi / 180
                        print(f"Cosine ({angle}\u00B0) = {degree}")
                        break
                    elif value in options and value == "r" or value == "R":
                        radians = degree * (pi/180)
                        print(f"Cosine ({angle}rad) = {radians}")
                        break
            except ValueError:
             print("Invalid input!")
    except ValueError:
        print("Invalid input!")