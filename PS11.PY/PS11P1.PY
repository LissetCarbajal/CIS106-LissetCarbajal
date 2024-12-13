


class Employee:
  
   def __init__(self, first, last, pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '.' + last + '@company.com'

   def fullname(self):
       return '{} {}'.format(self.first, self.last)

  def compute_bonus(self, bonus_rate):
    """Calculate the bonus as rate * salary."""
    return self.pay * bonus_rate


#Create instances of Employee
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname()
print(Employee.fullname(emp_1))
# print(emp_2.fullname())


Corey Schafer Bonus: $5000.00
Test User Bonus: $6000.00