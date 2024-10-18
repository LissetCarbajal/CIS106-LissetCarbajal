print ("Enter the name of appliance")
appliance=str(input())
print ("Enter the cost of appliance")
cost=float(input())
if cost>1000:
  warranty=cost*0.1
  if cost<=1000:
    warranty=cost*0.05
    total=cost+warranty
    print("Cost of appliance is $",cost)
    print("Warranty is $",warranty)
    print("Total is $",total)
    print("name of appliance is",appliance")