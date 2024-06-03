# Number Analysis Program
# Author: R. Dillard Coffey
def main():
  # Ask the user to enter a series of 20 numbers
  numbers = []
  for i in range(20):
    while True:
      try:
        number = float(input(f"Enter number {i + 1}: "))
        break
      # If the user enters a non-numeric value, display an error message and ask them to try again
      except ValueError:
        print("Please enter a valid number.")

    numbers.append(number)

  # Display the lowest number in the list
  lowest = min(numbers)
  print(f"The lowest number is: {lowest}")

  # Display the highest number in the list
  highest = max(numbers)
  print(f"The highest number is: {highest}")

  # Display the total of the numbers in the list
  total = sum(numbers)
  print(f"The total of the numbers is: {total}")

  # Display the average of the numbers in the list
  average = total / len(numbers)
  print(f"The average of the numbers is: {average}")


if __name__ == "__main__":
  main()
