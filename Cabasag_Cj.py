while True:
    
    print("\n=== Distance-Speed-Time Calculator ===")
    print (" 1. Compute Time ( Distance / Speed ) ")
    print(" 2. Compute Distance ( Speed x Time ) ")
    print(" 3. Compute Speed ( Distance / Time  ) ")
    print( " 4. Exit")

    choice = input( " Choose an Option (1-4): ")
    
    if choice == "1":
        distance = float(input(" Enter Distance in (km): "))
        speed = float(input(" Enter Speed in (km/hr): "))
        time = distance / speed
        print(f" Time Required: {time: .2f} hours")

    elif choice == "2":
        speed = float(input(" Enter Speed in (km/hr): "))
        time = float(input(" Enter Time in (hr): "))
        distance = speed * time
        print(f" Time Required: {distance: .2f} hours")
    elif choice == "3":
        distance = float(input(" Enter Speed in (km): "))
        time = float(input(" Enter Time in (hr): "))
        speed = distance / time
        print(f" Time Required: {distance: .2f} hours")
    elif choice == "4":
        print(" Exiting Distance-Speed-Time Calculator. Goodbye! ")

    else:
        print(" Invalid Choice. Please Enter a Number from 1-4")
