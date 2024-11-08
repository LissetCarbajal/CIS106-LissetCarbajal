#create text file with employee last name and salary
with open ("employee text file.txt", "w"))
file. write("Johnson, 50000\n")
file. write("Smith, 60000\n")
file. write("Williams, 70000\n")
file. write("Brown, 80000\n")
file. write("Jones, 90000\n")
total_bonus = 0
print(f"Last Name\tSalary\tBonus\tTotal")
with open("employee text file.txt", "
for line in file:
last_name, salary = line.strip().split(", ")
bonus = float(salary) * 0.10
total = float(salary) + bonus
total_bonus += bonus
if salary >=100000:
    bonus_rate = 0.20
if salary == 50000:
    bonus_rate = 0.15
print(f"{last_name}\t{salary}\t{bonus:.2f}\t{total:.2

  