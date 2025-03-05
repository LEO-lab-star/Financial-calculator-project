from loan_calculator import loan_calculator
from compound_interest_calculator import compound_interest_calculator
from savings_growth import savings_growth

def main():
    print("Financial Calculator")
    print("1. Loan Payment Calculation")
    print("2. Compound Interest Calculation")
    print("3. Savings Growth Calculation")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        principal = float(input("Enter loan amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter loan term (years): "))
        print(f"Monthly Payment: {loan_payment(principal, rate, years)}")
    
    elif choice == '2':
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        times_per_year = int(input("Enter times interest is compounded per year: "))
        years = int(input("Enter time (years): "))
        print(f"Future Value: {compound_interest(principal, rate, times_per_year, years)}")
    
    elif choice == '3':
        initial_savings = float(input("Enter initial savings: "))
        monthly_contribution = float(input("Enter monthly contribution: "))
        rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter time (years): "))
        print(f"Total Savings: {savings_growth(initial_savings, monthly_contribution, rate, years)}")
    
    else:
        print("Invalid choice. Please restart.")

if __name__ == "__main__":
    main()
