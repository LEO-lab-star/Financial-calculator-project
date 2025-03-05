import math

def loan_payment_calculator(principal, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = loan_term_years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -number_of_payments))
    return monthly_payment

# Get user input
def main():
    print("Welcome to the Loan Payment Calculator!")
    
    # Input for the principal amount
    principal = float(input("Enter the loan amount (principal): $"))
    
    # Input for the annual interest rate
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    
    # Input for the loan term in years
    loan_term_years = int(input("Enter the loan term (in years): "))
    
    # Calculate monthly payment
    monthly_payment = loan_payment_calculator(principal, annual_interest_rate, loan_term_years)
    
    # Output the result
    print(f"Monthly Loan Payment: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()