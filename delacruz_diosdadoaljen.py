def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_up_to_limit(limit):
    """Return a list of prime numbers up to a given limit."""
    return [i for i in range(2, limit + 1) if is_prime(i)]

def main():
    while True:
        print("\n=== Prime Number Utility ===")
        print("1. Check if a number is prime")
        print("2. Show all primes up to a limit")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            number = int(input("Enter an integer (>1): "))
            if is_prime(number):
                print(f"{number} is prime.")
            else:
                print(f"{number} is not prime.")
        
        elif choice == "2":
            limit = int(input("Enter the upper limit (>1): "))
            primes = primes_up_to_limit(limit)
            print(f"Primes up to {limit}: {primes}")
        
        elif choice == "3":
            print("Exiting Prime Number Utility. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")