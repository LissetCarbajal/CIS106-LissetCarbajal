#creat a text file with student last name, district code,number of credits
open (student file.txt, "w")
file.write("Smith, A, 10\n")
file.write("Johnson, B, 20\n")
file.write("Williams, A, 15\n")
file.write("Brown, B, 25\n")
file.write("Jones, A, 5\n")
total_tuition = 0
student_count = 0
print(f"Last Name\tDistrict Code\tCredits\tTuition"))
with open("student file.txt", "r") as file:
for line in file:
last_name, district_code, credits = line.strip().split(",
credits = int(credits)
if district_code == "I":
 cost_per_credit = 250.00
else if district_code == "O":
 cost_per_credit = 500.00
tuition = cost_per_credit * credits
total_tuition += tuition
student_count += 1
print(f"{last_name}\t{district_code}\t{credits}\t{tuition:.2
