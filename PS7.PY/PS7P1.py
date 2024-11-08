principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
total_interest = 0
print("Year\tPrincipal\tInterest\tBalance")
for year in range(1, 6)
interest = principal * rate
ending_balance = principal + interest
print(f"{year}\t{principal:.2f}\t{interest:.2f}\t
total_interest += interest
principal = ending_balance
print(f"Total interest earned: {total_interest:.2
repeat = input("Do you want to repeat the program? (y/n): ")
if repeat.lower() != "y":
break
