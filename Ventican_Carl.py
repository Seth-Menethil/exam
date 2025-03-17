print("=== Loan Payment Calculator ===\n1. Compute Monthly Payment\n2. Exit")
choice=int(input("Choose an option (1-2): "))
while choice == 1:
    loanPrincipal=float(input("Enter loan principal: "))
    interestRate=float(input("Enter annual interest rate (in %): "))
    loandurationYears=float(input("Enter loan duration in years: "))