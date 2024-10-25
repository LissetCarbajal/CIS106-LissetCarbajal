print ("Enter the item to be purchased")
item = input()
print ("Enter the quantity")
quantity = int(input())
if item == "10":
  unitprice = 1.00
else:
  if item=="55":
    unitprice = 1.00
else:
  if item=="99":
    unitprice = 2.00
else:
  if item=="80":
    unitprice = 3.00
  else:
    if item =="70":
      unitprice = 3.00
  else:
    unitprice = 5.00
#compute price
price = quantity