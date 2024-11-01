control = str(input("Enter Yes if you would like to run this program "))
x=0
while control == "Yes":
  name = str(input("Enter the Student's name "))
  midterm = float(input("Enter the student's midterm exam grade "))
  final = float(input("Enter the student's final exam grade "))
  average = (midterm + final)/2
  print(name, "has an average of ", average
  x=x+1
  control = str(input("Enter Yes if you would like to run this program "))
print("You have run this program", x, " times")