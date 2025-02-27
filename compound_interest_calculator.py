import math

def compound_interest_calculator(principal, annual_interest_rate, times_compounded_per_year, years):
    future_value = principal * math.pow((1 + annual_interest_rate / times_compounded_per_year / 100), times_compounded_per_year * years)
    return future_value

# Get user input
def main():
    print("Welcome to the Compound Interest Calculator!")
    
    # Input for the principal amount
    principal = float(input("Enter the principal amount: $"))
    
    # Input for the annual interest rate
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    
    # Input for the number of times interest is compounded per year
    times_compounded_per_year = int(input("Enter the number of times interest is compounded per year: "))
    
    # Input for the number of years
    years = int(input("Enter the number of years: "))
    
    # Calculate future value
    future_value = compound_interest_calculator(principal, annual_interest_rate, times_compounded_per_year, years)
    
    # Output the result
    print(f"Future Value of the Investment: ${future_value:.2f}")

if __name__ == "__main__":
    main()