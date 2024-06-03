# Miles to Kilometers Converter
# Author: R. Dillard Coffey


def miles_to_kilometers(miles):
  # 1 mile is approximately 1.60934 kilometers
  return miles * 1.60934


def get_valid_miles():
  while True:
    try:
      # Prompt the user to enter a distance in miles
      miles = float(input("Enter the number of miles driven: "))
      # Check if the input is a positive number
      if miles < 0:
        raise ValueError("number entered was negative")
      return miles
    # Print an error message if the input is not a valid number
    except ValueError as e:
      print(f"Error: {e}, please enter a positive number.")


# Main function
def main():
  print("Miles to Kilometers Converter\n\n")
  # Get valid input for miles driven
  miles = get_valid_miles()
  # Convert miles to kilometers
  kilometers = miles_to_kilometers(miles)
  # Display the total miles and kilometers
  print(f"Total miles: {miles}")
  print(f"Total kilometers: {kilometers:.2f}")


# Run the main function
if __name__ == "__main__":
  main()
