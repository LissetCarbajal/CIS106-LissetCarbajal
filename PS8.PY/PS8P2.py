def calculate_batting_avg(hits, at_bats)
 batavg=hits/at_bats
 return batavg



for count in range(1,10,1)
 name=input("Enter the player's name ")
 hits=int(input("Enter the number of hits the player had ")
 atbats=int(input("Enter the number of times the player battled ")
 batavg=calculate_batting_avg(hits, atbats)
 print("Player ", name, "Batting average is ",batavg)
print("Total number of player", count)