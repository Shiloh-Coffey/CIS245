# Student Cumulative GPA Calculator
# Author: R. Dillard Coffey
class Student:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.grade_point = 0
    self.credits = 0
    self.gpa = 0

  def CalculateGPA(self, grade, credits):
    self.grade_point += grade * credits
    self.credits += credits
    self.gpa = self.grade_point / self.credits

  def GetGPA(self):
    return self.gpa


# Prompt the user for the first and last name of the student
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

# Create a student object
student = Student(first_name, last_name)

# Create a loop to input course information
while True:
  credits = float(
      input("Enter the credits for the course (input 0 to quit): "))
  if credits == 0:
    break
  grade = float(input("Enter the grade points for the course (0.0 - 4.0): "))
  student.CalculateGPA(grade, credits)

# Display the student's cumulative GPA
print(
    f"{student.first_name} {student.last_name}'s cumulative GPA is: {student.GetGPA():.2f}"
)
