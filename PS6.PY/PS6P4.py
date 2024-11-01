response = input("Do you want to enter employee data? (Yes to continue): ")
while response == "Yes":
    name = input("Enter employee name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    gross = hours * rate
if hours worked > 40:
    regular pay = 40 * rate
    overtime pay = (hours worked - 40) * (rate * 1.5)
    gross = regular pay + overtime pay
else:
    gross = hours worked * rate
print("Employee name: ", name)
print("Gross pay: $", gross)
total gross pay += gross
employee count += 1
response = input("Do you want to enter employee data? (Yes to continue): ")
if employee count > 0:
  average gross pay = total gross pay / employee count
  print("sum of all the gross pay: $"))
  print("number of employees: ", employee count)")
  print("average gross pay: $", average gross pay)