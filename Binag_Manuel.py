x=0

while True:
    print("1) Generate the Collatz sequence for a positive integer\n2)Exit.")
    n=int(input("Choose an option (1-2): "))
    if n == 1:
        x=int(input("\nEnter a Positive integer: ")) 
        while x != 1:
            print("Collatz sequence: ", x)
            if x % 2 == 0:
                x=x/2
            else:
                x=(3*x)+1
        print("Collatz sequence: ", x)
    elif n == 2:
        print("Exiting collatz Menu. Goodbye!")
        break;
else:
    print("Input 1 or 2 only!")