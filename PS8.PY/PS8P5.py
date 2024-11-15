def compute_tuition(credit_hours, district_code)
#Compute tuition based on credit hours and district code. In-district ('I') is $250 per credit hour, out-of-district ('O') is $550 per credit hour.)
rates = {'I': 250, 'O': 550}
rate_per_hour = rates.get(district_code.upper(), 0)
credit_hours * rate_per_hour

#Initialize total tuition variable
total_tuition = 0
while True:
  last_name = input("Enter student's last name: ")
  district_code = input("Enter district code (I or O): ")
  credit_hours = int(input("Enter number of credit hours: "))
  tuition = compute_tuition(credit_hours, district_code)
  print(f"{last_name}'s tuition is: $ {tuition:.2f}")
  total_tuition += tuition
  if input("Do you want to continue? (y/n)").lower() != "y":
    break
print(f"Total tuition for all students: $ {total_tuition:.2f}")