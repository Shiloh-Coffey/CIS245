"""
Name: Inventment Doubling Calculator
Author: R. Dillard Coffey
Description: This script calculates the number of years it takes for an investment to double at a given interest rate.
"""


# Calculate the number of years to double the investment
def years_to_double_investment(interest_rate, initial_investment):
  current_balance = initial_investment
  years = 0

  while current_balance < 2 * initial_investment:
    current_balance += current_balance * (interest_rate / 100)
    years += 1

  return years


# Input validation
def get_positive_float(prompt):
  while True:
    try:
      value = float(input(prompt))
      if value <= 0:
        raise ValueError
      return value
    except ValueError:
      print("Please enter a positive number.")


# Get user input for interest rate and initial investment
interest_rate = get_positive_float("Enter the interest rate (in percentage): ")
initial_investment = get_positive_float(
    "Enter the initial investment amount: ")
# Call the function to calculate the number of years
years = years_to_double_investment(interest_rate, initial_investment)
# Display the result
print(f"It will take {years} years for the investment to double.")
