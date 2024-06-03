# User Information Storage System
# Author: R. Dillard Coffey
def main():
  # Prompt the user for the file name
  file_name = input("Enter the file name (without extension): ")
  # Makes sure .txt is the only file extension
  while not file_name or "." in file_name:
    print("File name cannot be empty and must not contain an extension.")
    file_name = input("Enter the file name (without extension): ")

  # Prompt the user for their name
  name = input("Enter your name: ")
  while not name:
    print("Name cannot be empty.")
    name = input("Enter your name: ")

  # Prompt the user for their street address
  street_address = input("Enter your street address: ")
  while not street_address:
    print("Street address cannot be empty.")
    street_address = input("Enter your street address: ")

  # Prompt the user for their phone number
  phone_number = input("Enter your phone number: ")
  while not phone_number:
    print("Phone number cannot be empty.")
    phone_number = input("Enter your phone number: ")

  # Add a .txt extension to the file name
  file_name += ".txt"

  # Write the user's information to the file
  with open(file_name, 'w') as file:
    file.write(f"{name},{street_address},{phone_number}\n")

  # Read the file and display its contents
  with open(file_name, 'r') as file:
    contents = file.read()
    print("\nFile contents:")
    print(contents)


if __name__ == "__main__":
  main()
