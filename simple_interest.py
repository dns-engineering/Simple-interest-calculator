def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

if __name__ == "__main__":
    
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    
    interest = calculate_simple_interest(principal, rate, time)
    print(f"The simple interest is: {interest}")
