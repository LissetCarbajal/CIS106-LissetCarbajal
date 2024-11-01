response = input("Do you want to enter order data? (Yes to continue): ")
while response == "Yes":
  quantity = int(input("Enter the quantity of the item: "))
  price = float(input("Enter the price of the item: "))
  extended_price = quantity * price
  if extended_price > 10000.00:
    discount = extended_price * 0.10
  else:
    discount = 0.00
  total = extended_price - discount
  print("Extended price: $", extended_price)
  print("Discount: $", discount)
  print("Total: $", total)