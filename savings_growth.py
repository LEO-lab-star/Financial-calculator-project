def calculate_savings_growth(initial_savings, monthly_contribution, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_months = years * 12

    future_value = initial_savings * (1 + monthly_interest_rate) ** total_months

   
    for month in range(1, total_months + 1):
        future_value += monthly_contribution * (1 + monthly_interest_rate) ** (total_months - month)

    return future_value

# User inputs
try:
    initial_savings = float(input("Enter initial savings amount: "))
    monthly_contribution = float(input("Enter monthly contribution amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter the number of years: "))

    # Calculate future value
    future_value = calculate_savings_growth(initial_savings, monthly_contribution, annual_interest_rate, years)

    # Output the result
    print(f"\nFuture value of savings after {years} years: NLe{future_value:.2f}")

except ValueError:
    print("Please enter valid numeric inputs.")
