data = [
    [1000, 600, 8000, 5000],  # Row 1
    [2000, 1200, 10000, 7000],  # Row 2
    [1500, 800, 9000, 6000],  # Row 3
]
# This is our demo data to use for this. Assume it could be dollars, gold doubloons, doesn't matter.

# Initialize totals
total_revenue = 0
total_expenses = 0
total_assets = 0
total_liabilities = 0

# Handling each of the rows:
for row in data:
    total_revenue += row[0]
    total_expenses += row[1]
    total_assets += row[2]
    total_liabilities += row[3]

# Calculations:
total_profit = total_revenue - total_expenses  # Net Income
total_equity = total_assets - total_liabilities  # Equity
profit_margin = (total_profit / total_revenue) * 100 if total_revenue else 0

# Print results:
print(f"Total Revenue: ${total_revenue}")
print(f"Total Expenses: ${total_expenses}")
print(f"Net Income (Profit): ${total_profit}")
print(f"Total Assets: ${total_assets}")
print(f"Total Liabilities: ${total_liabilities}")
print(f"Equity: ${total_equity}")
print(f"Profit Margin: {profit_margin:.2f}%")
