"""
- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""

days = int(input("how many days until your birthday? "))
days_per_week = 7
weeks_remainings = round(days/days_per_week,2)

print(f"Weeks remainings... {weeks_remainings}")