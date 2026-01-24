"""
- You have $50
- You buy an item that cost $15
- With a tax of 3%
- Print how much money you have left
"""

money = 50
cost = 15
tax = .03

money_left = money - cost -(cost*tax)
print(f"El dinero restante es {money_left}")