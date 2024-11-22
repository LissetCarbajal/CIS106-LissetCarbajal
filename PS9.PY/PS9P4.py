#Function to load player names and batting averages from a file
def load_players(file_name):
  player_names = []
  batting_averages = []

with open(file_name, "r") as file:
  for line in file:
    name, average = line.strip().split(",")
    player_names.append(name)
    batting_averages.append(float(average))
 
player_names, batting_averages

#Function to display the player names and batting averages
def display_players(names, averages):
  print("Player Names and Batting Averages:")
  for name, average in zip(names, averages):
    print(f"{name}: {average:.3f}")

#Function to search for a player by last name and display the batting average
def search_player(names, averages, search_name):
  for name, in average in zip(names, averages):
    if name.lower() == search_name.lower():
      print(f"Player Found: {name} with a batting average of {average:.3f}")
      return
  print("Player not found.")

#Main program
file_name = "players.txt"

#Load data from the file
player_names, batting_averages = load_players(file_name)

#Display all players and batting averages
display_players(player_names, batting_averages)
print()

#Search loop
while True:
  search_name = input("Enter a player's last name to search (or 'quit' to exit):
  if search_name.lower() == "exit":
     print("Exiting the program. Goodbye!")
      break
  search_player(player_names, batting_averages, search_name)
  print()