print ("Enter the number of books to order")
numbooks=int(input())
print ("Enter the cost of the book")
costbooks=float(input())
if ordertotal>50:
  shipping=0
  if ordertotal<=50:
    shipping=25
    order total=number of books*costbooks+shipping
    print("Order total is $",ordertotal)
    print("Shipping is $",shipping)