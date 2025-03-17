print("=== Loan Payment Calculator ===\n1. Compute Monthly Payment\n2. Exit")
choice=int(input("Choose an option (1-2): "))
while choice == 1:
    P=str(input("Enter loan principal: "))
    r=str(input("Enter annual interest rate (in %): "))
    n=int(input("Enter loan duration in years: "))