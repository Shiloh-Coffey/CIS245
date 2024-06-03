# Fiber Optic Cable Installation Cost Calculator
# Author: R. Dillard Coffey

#Display a welcome message
print("Welcome to the Coffey Fiber Optics Co.'s Installation Cost Calculator!")

#Initialize the cost per foot and the company's name
costPerFoot = 0.87
companyName = "Coffey Fiber Optics Co."

#Enter loop
while True:
  try:
    #Capture the number of feet of fiber optic to be installed from the user
    cableToInstall = float(
        input("Enter the number of feet of fiber optic cable to install: "))
    #Check to make sure the number is greater than 0
    if cableToInstall <= 0:
      print("Please enter a positive number that is greater than 0.")
      continue

    #Calculate the total cost
    totalCost = cableToInstall * costPerFoot

    #Using string formating, display the calculated information and company name, .2f is used to round to 2 decimal places
    print(
        f"For {cableToInstall} feet the total installation cost by {companyName} will be ${totalCost:.2f}."
    )
    #Exit the loop if input is a float
    break
  #If the input isn't a float then the loop will restart
  except ValueError:
    print("Please enter a valid number.")
