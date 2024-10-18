#Compute total cost
item=str(input("Enter the item must be A or B"))
quan=int( input("Enter the quantity "))
if item=="A":
  unitprice=10
else:
  unitprice=20
total=quan*unitprice
print(f"Item:{item} Quantity:{quan} Unit Price: ${unitprice:.2f} Total: ${total:.2f}")