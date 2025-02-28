def savings_growth(initial_savings, monthly_contribution, rate, years):
    months = years * 12
    monthly_rate = rate / 100 / 12
    future_value = initial_savings * (1 + monthly_rate) ** months
    for i in range(1, months + 1):
        future_value += monthly_contribution * (1 + monthly_rate) ** (months - i)
    return round(future_value, 2)
