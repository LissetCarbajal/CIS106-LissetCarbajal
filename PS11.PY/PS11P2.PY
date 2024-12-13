class Student:
  def__init__(self, first_name, last_name, district_code, enrolled_credits):

Initializes a new Student object.

Attributes:
first_name (str): The first name of the student.
last_name (str): The last name of the student.
district_code (str): The district code of the student (I for in-district, O for out-of-district).
enrolled_credits (int): The number of credits the student is enrolled in.

self.first_name = first_name
self.last_name = last_name
self.district_code = district_code.upper()
self.enrolled_credits = enrolled_credits

def compute_tuition_owed(self):

 Computes the tuition owed by the student based on the district code and enrolled credits.

  Returns:
  float: The total tuition owed.

rate_per_credit = 250.00 if self.district_code == 'I' else 500.00
return self.enrolled_credits * rate_per_credit

def __str__(self);

  Returns a string representation of the student object;

  Returns:
  str: A formatted string with student detatils and tuition owed.

tuition_owed= = self.compute_tuition_owed()
return f"Name: {self.first_name} {self.last_name}\nDistrict Code:
