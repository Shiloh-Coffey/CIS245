# Fiber Optic Cable Installation Cost Calculator
# Author: R. Dillard Coffey

# Display a welcome message
print("Welcome to the Coffey Fiber Optics Co.'s Installation Cost Calculator!")

# Initialize the company's name
companyName = "Coffey Fiber Optics Co."

# Enter loop
while True:
  try:
    # Capture the number of feet of fiber optic cable to be installed from the user
    cableToInstall = float(
        input("Enter the number of feet of fiber optic cable to install: "))
    # Check to make sure the number is greater than 0
    if cableToInstall <= 0:
      print("Please enter a positive number that is greater than 0.")
      continue

    # Determine the cost per foot based on the amount purchased
    if cableToInstall > 500:
      costPerFoot = 0.50
    elif cableToInstall > 250:
      costPerFoot = 0.70
    elif cableToInstall > 100:
      costPerFoot = 0.80
    else:
      costPerFoot = 0.87  # Default cost for less than or equal to 100 feet

    # Calculate the total cost
    totalCost = cableToInstall * costPerFoot

    # Using string formatting, display the calculated information and company name, .2f is used to round to 2 decimal places
    print(
        f"For {cableToInstall} feet, the total installation cost by {companyName} will be ${totalCost:.2f}."
    )
    # Exit the loop if input is a float
    break
  # If the input isn't a float then the loop will restart
  except ValueError:
    print("Please enter a valid number.")
