import csv

############### this is basically a recall / search function for our csv file - containing a roster of active and inactive ufc fighters and stats. 
############### use their names, in this case Calvin Katter, at index 1526 to display their row of stats.
############### now lets use this functionality to pull in two fighters and bring their stats vs each other.

fighterID_one = input('Who is fighting: [Capitalized or Lowercase: First and Last Name]: ').title()
fighterID_two = input("Who is " + fighterID_one + " fighting against? ").title()
print("")
fightdisplay = print(fighterID_one + " vs " + fighterID_two)
print("")

#stats check
print('\  Checking Stats')

# fighterID = input('UFC Fighter [Capitalized or Lowercase: First and Last] Name: ').title()
def find_index(input): 
    o = open('purestats2.csv', 'r') 
    ufcroster = csv.reader(o) 
    index = 0 
    for row in ufcroster:
      #print row
      if row[1] == input: 
        return index 
      else : index+=1
    
f1 = find_index(fighterID_one)
f2 = find_index(fighterID_two)

if f1 == None:
  print(f'Issue with the name {fighterID_one}, check the first and last name and start over')
elif f2 == None:
  print(f'Issue with the name {fighterID_two}, check the first and last name and start over')

# calvin kattar = 1526
# vs
# dan ige = 1360

####### lines.py

# Open the file.
# Use the open file as a parameter into csv.reader().
file = open("purestats2.csv")

reader = csv.reader(file)

# Iterate over ufc roster
roster = []
for row in reader:
    roster.append(row)

print('')
print(roster[f1])
print(roster[f2])

############### this is basically a recall / search function for our csv file - containing a roster of active and inactive ufc fighters and stats. 
############### use their names, in this case Calvin Katter, at index 1526 to display their row of stats.
############### now lets use this functionality to pull in two fighters and bring their stats vs each other.