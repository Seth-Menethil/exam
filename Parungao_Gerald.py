
while True:
    
    print("\n=== Temperature Converter ===")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

    
    option = input("Choose an option (1-3): ")

    if option == '1':
        
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")
        
    elif option == '2':
        
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius:.1f}°C")
        
    elif option == '3':
       
        print("Exiting Temperature Converter. Goodbye!")
        break
        
    else:
        
        print("Invalid choice! Please select option 1, 2, or 3.")

