# Student Cumulative GPA Calculator
# Author: R. Dillard Coffey


class Student:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.grade_points = 0
    self.credits = 0
    self.gpa = 0

  def calculate_gpa(self, grade, credits):
    self.credits += credits
    if grade == 'A':
      self.grade_points += credits * 4
    elif grade == 'B':
      self.grade_points += credits * 3
    elif grade == 'C':
      self.grade_points += credits * 2
    elif grade == 'D':
      self.grade_points += credits * 1
    else:
      self.grade_points += credits * 0
    self.gpa = self.grade_points / self.credits

  def get_gpa(self):
    return round(self.gpa, 1)


class DeclaredStudent(Student):

  def __init__(self, first_name, last_name, concentration):
    super().__init__(first_name, last_name)
    self.concentration = concentration

  def get_year(self):
    if self.credits < 30:
      return 'Freshman'
    elif 30 <= self.credits < 60:
      return 'Sophomore'
    elif 60 <= self.credits < 90:
      return 'Junior'
    else:
      return 'Senior'

  def display_info(self):
    print(
        f'The GPA for {self.first_name} {self.last_name}, concentrating in {self.concentration}, is {self.get_gpa()}'
    )
    print(f'The student is a {self.get_year()}')


# Main program
student_first_name = input('Please enter the student first name: ')
student_last_name = input('Please enter the student last name: ')
student_concentration = input(
    'Please enter the student declared concentration: ')

declared_student = DeclaredStudent(student_first_name, student_last_name,
                                   student_concentration)

quit = '1'
while quit == '1':
  grade = input('Please enter student grade: ')
  credits = int(input('Please enter credits: '))
  declared_student.calculate_gpa(grade, credits)
  quit = input('Press 1 to continue entering grades or 2 to quit: ')

declared_student.display_info()
