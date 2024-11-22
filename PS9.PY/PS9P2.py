last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

#Assign exam scores for the respective students
exam_scores = [85, 92, 78, 88, 95, 90, 76, 82, 89, 91]

#Function to display the names along with their exam scores
def display_names_and_scores(names, scores):
  print("Names and Exam Scores in Order:")
  for name, score in zip(names, scores):
    print(f"{name}: {score}")

#Function to display the names and exam scores in reverse order
def display_names_scores_reverse(names, scores):
  print("Names and Exam Scores in Reverse Order:")
  for name, score in zip(reversed(names), reversed(scores)):
    print(f"{name}: {score}")

#Call the functions
display_names_and_scores(last_names, exam_scores)
print() #Print a blank line for better readability
display_names_and_scores_reverse(last_names, exam_scores)