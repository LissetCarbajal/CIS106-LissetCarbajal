print ("Enter last name")
lastname=str(input())
print ("Enter the number of dependents")
dependents=int(input())
print ("Enter the gross income")
grossincome=float(input())
grossincome-dependents*12000
if grossincome>=50000:
  taxrate=0.2
  if grossincome<50000:
    taxrate=0.1
income tax=grossincome*taxrate
if income tax<0:
  income tax=100
print ("Last name is",lastname")
print ("Gross income is $",grossincome)
print ("Number of dependents is",dependents)
print ("Adjusted gross income is $",grossincome-dependents*12000")
print ("Income tax is $",income tax)