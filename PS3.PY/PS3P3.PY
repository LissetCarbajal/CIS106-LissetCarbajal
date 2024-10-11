print( "Enter how much did you pay for your meal") #Asking user how much they paid for their meal
meal = float(input())
tip15 = meal*.15 #Calculating 15% tip
tip18 = meal*.18
tip20 = meal*.20
meal_str = " {:,.2f}".format(meal)
#printing With 15% tip
print("with 15% tip:", "\n Total:" "(:.2F)".format(meal), "\n Tip:", "(:.2F)".format(tip15), "\n Total with tip:","(:.2F)".format(meal+tip15))
print("With 18% tip:", "\n Total:" "(:.2F)".format(meal), "\n Tip:","(:.2F)".format(tip18), "\n Total with tip:", "(:.2F)".format(meal+tip18))
print("With 20% tip:", "\n Total:" "(:.2F)".format(meal), "\n Tip:","(:.2F)".format(tip20), "\n Total with tip:", "(:.2F)".format(meal+tip20)