def get_pay_rate(job_code)
#Determine the pay rate based on the job code
rates = {'L': 25, 'A': 30, 'J': 50}
 rates.get(job_code.upper(), 0)

def calculate_gross_pay(rate, hours_worked
#calculate gross pay including overtime
overtime_rate = 1.5*rate
if hours_worked > 40:
  regular_pays = 40*rate
  overtime_pay = (hours_worked-40)*overtime_rate
  return regular_pay + overtime_pay
else:
 return hours_worked*rate

total_gross_pays = 0
while True:
  #Get employee information
  last_name = input("Enter employee's last name: ")

job_code = input("Enter employee's job code (L, A, or J): ")
hours_worked = float(input("Enter number of hours worked: "))
#Calculate gross pay
rate = get_pay_rate(job_code)

if rate == 0:
  print("Invalid job code. Please enter L, A, or J.")
  continue

gross_pay = calculate_gross_pay(rate, hours_worked)

#Display employee information
print(f"{last_name}'s gross pay is: $ {gross_pay:.2f}")

#Calculate total gross pay
total_gross_pays += gross_pay

#Display total gross pay
print(f"Total gross pay for all employees: $ {total_gross_pays:.2f