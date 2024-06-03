# Initials Extractor From Full Name
# Author: R. Dillard Coffey


def main():
  while True:
    # Get the full name from the user
    full_name = input("Enter your full name: ")

    # Check if the input is empty
    if not full_name:
      print("Error: Please enter a valid full name.")
      continue

    # Call the get_initials function with the input name and print the result
    initials = get_initials(full_name)
    if initials:
      print("Initials:", initials)
      break
    else:
      print(
          "Error: Please enter a valid full name with at least a first and last name."
      )


# Define a function that takes a string containing a person's full name
# and returns their first, middle, and last initials
def get_initials(name):
  # Split the input string into individual names
  names = name.split()

  # Check if there are at least 2 names in the input
  if len(names) < 2:
    return None

  # Extract the first letter of each name and add a period after it
  initials = [name[0].upper() + '.' for name in names]

  # Join the initials together with a space in between
  return ' '.join(initials)


if __name__ == "__main__":
  main()
