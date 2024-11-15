def calculate_mpg(miles, gaallons):
#calculate miles gallon
if gallons == 0:
 mpg = 0


def main()
trip_count = 0
while True:
#get miles driven
 destination = input("Enter the destination of the trip: ")
 if destination.lower() == "done"

  miles = float(input("Enter the number of miles driven: "))
  gallons = float(input("Enter the number of gallons used: "))
#compute MPG
 mpg = calculate_mpg(miles, gallons)
#display MPG
 print(f"Destination: {destination}, Miles Traveled: {miles}, Gallons Used: {gallons}, MPG: {mpg}")
#increment trip count
 trip_count += 1
#check if user wants to continue
 if input("Do you want to continue? (y/n)").lower() != "y":