daily_sales = [5, 45, 68, 51, 36, 54, 21, 35, 12, 1, 3, 53]

totals_cups = sum(sale for sale in daily_sales if sale > 15)
print(totals_cups)
