def calculate_total(quantity, price)
total = quantity * price
if total > 10000:
 total = total-(total*0.10)
total

eprice=0
loop = input("Do you want to run this program? Enter Yes or No ")
while loop == "Yes":
 quantity=int(input("Enter the quantity "))
 price=float(input( "Enter the price "))
 #call the function
 total=calculate_total(quantity,price
 #print value returned from function
 print("Quantity purchased ", quantity,   "Price per unit $", "{:.2F}".format(price), "Total $", "{:.2F}".format(total)")
 eprice=eprice+total
 loop = input("Do you want to run this program? Enter Yes or No ")
print("Total of all entries $", "{:.2F}".format(eprice))