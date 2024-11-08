# create text file with item, quantity, and price
# with open("item_prices.txt", "w") as file:
# file.write("Item1, 10, 5.99\n")
# file.write("Item2, 20, 9.99\n")
# file.write("Item3, 5, 12.99\n")
# file.write("Item4, 15, 7.49\n")
total_extenal_price = 0
order_count = 0
print(f"Item\tQuantity\tPrice\tExt. Price"
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item
extended_price = price * quantity
total_extenal_price += extended_price
order_count += 1
print(f"{item}\t{quantity}\t{price:.2f}\t
average_order = total_extenal_price / order_count
print(f"Total extended price: {total_ext