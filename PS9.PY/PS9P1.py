#Assign 10 last names to an array
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
#Function to display the names
def display_names(last_names):
  print("Last Names in order:")
  for name in names:
     print(name)

#Function to display the names in reverse order
def display_reverse_order(last_names):
  print("Names in reverse order:")
  for name in reversed(names):
    print(name)

#Call the functions
display_names(last_names)
print() #Print a blank line for better readability
display_names_reverse(last_names)