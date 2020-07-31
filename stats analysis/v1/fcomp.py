import csv

############### this is basically a recall / search function for our csv file - containing a roster of active and inactive ufc fighters and stats. 
############### use their names, in this case Calvin Katter, at index 1526 to display their row of stats.
############### now lets use this functionality to pull in two fighters and bring their stats vs each other.

fighterID_one = input('Who is fighting: [Capitalized or Lowercase: First and Last Name]: ').title()
fighterID_two = input("Who is " + fighterID_one + " fighting against? ").title()
print("")
fightdisplay = print(fighterID_one + " vs " + fighterID_two)


#stats check
print('---------------------')
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

# if an error if naming, or the file itself has a certain vanaming convention inside of it...
# will cause errors, try to catch the mispelling in w/ this if statement.
if f1 == None:
  print("")
  print(f'ISSUE: {fighterID_one}, check the first and last name and start over')
  fighterID_one = input(f"{fighterID_one}, rename: ").title()
elif f2 == None:
  print("")
  print(f'ISSUE: {fighterID_two}, check the first and last name and start over')
  fighterID_two = input(f"{fighterID_two}, rename: ").title()

f1 = find_index(fighterID_one)
f2 = find_index(fighterID_two)

# calvin kattar = 1526 vs dan ige = 1360

####### lines.py

# Open the file.
# Use the open file as a parameter into csv.reader().
file = open("purestats2.csv")

reader = csv.reader(file)

# Iterate over ufc roster
roster = []
for row in reader:
    roster.append(row)


def score():
  if f1point > f2point:
    print('---------------------')
    print(f'With {f1point}, {fighterID_one} has the most avantages.')
  elif f1point == f2point:
    print(f'{f1point} + " Equal Stat Scores. " + {f2point}')
  else:    
    print('---------------------')
    print(f'With {f2point} points, {fighterID_two} has the most avantages.')


indexloop = 3
header = roster[0][indexloop]

f1point = 0
f2point = 0
def statcomp():
  global f1point
  global f2point
  if roster[f1][indexloop] > roster[f2][indexloop]:
    f1point = f1point + 1
    print(f"{header} | Point for {fighterID_one}")
  elif roster[f1][indexloop] == roster[f2][indexloop]:
    print(f"{header} | Equal. No Points.")
  elif roster[f1][indexloop] < roster[f2][indexloop]:    
    f2point = f2point + 1
    print(f"{header} | Point for {fighterID_two}")
    


# Defining the `calc_height` variable.
def calc_height(raw_height):
# Calculates height from feet-inches to inches
# Parameters
# ---------
# Variable, feet-inches raw_height: Raw Height for example, 5-10 or 5-2 or 5-9
  height_components = raw_height.split("-")
  n_feet = int(height_components[0])
  n_inches = int(height_components[1])

  return (n_feet * 12) + n_inches


#skip stance and dob
while indexloop <= 15:
  #print(roster[0][indexloop] + ": " + roster[f1][indexloop])
  #print(roster[0][indexloop] + ": " + roster[f2][indexloop])
  header = roster[0][indexloop]
  if indexloop == 3:
    f1h = calc_height(roster[f1][indexloop])
    f2h = calc_height(roster[f2][indexloop])
    if f1h > f2h:
      print(f"{header} | Point for {fighterID_one}")
    elif f1h == f2h:
      print(f"{header} | Equal. No Points.")
    elif f1h < f2h:
      print(f"{header} | Point for {fighterID_two}")
  if indexloop == 4:
    statcomp()
  if indexloop == 5:
    statcomp()
  if indexloop == 8:
    statcomp()
  if indexloop == 9:
    statcomp()
  if indexloop == 10:
    statcomp()
  if indexloop == 11:
    statcomp()
  if indexloop == 12:
    statcomp()
  if indexloop == 13:
    statcomp()
  if indexloop == 14:
    statcomp()
  if indexloop == 15:
    statcomp()
    score()
  indexloop += 1


# freach_one = roster[f1][5]
# freach_two = roster[f2][5]

# print('')
# print(fighterID_one + " " + roster[0][5] + ": " + freach_one)
# print(fighterID_two + " " + roster[0][5] + ": " + freach_two)

# This compares Takedown Accuracy
# print('')
# print(fighterID_one + " " + roster[0][13])
# print(roster[f1][13])
# print(fighterID_two + " " + roster[0][13])
# print(roster[f2][13])

# This compares Sig Strike Accuracy
# print('')
# print(fighterID_one + " " + roster[0][9])
# print(roster[f1][9])
# print('')
# print(fighterID_two + " " + roster[0][9])
# print(roster[f2][9])

############### Search function for our csv file - containing a roster of active and inactive ufc fighters and stats. 
############### use their names, in this case Calvin Katter, at index 1526 to display their row of stats.
############### now lets use this functionality to pull in two fighters and bring their stats vs each other.

# ['cap-date', 'name', 'record', 'height', 'weight', 'reach', 'stance', 'dob', 'slpm', 'stracc', 'sapm', 'strdef', 'tdavg', 'tdacc', 'tddef', 'subavg', '']
#       0         1       2         3         4         5         6      7       8        9        10       11        12      13       14        15

########################## this calculates the average of the column - reach 

reachlist = []

o = open('purestats2.csv', 'r') 
ufcroster = csv.reader(o) 
for reachavg in ufcroster:
  if reachavg[5] == None:
    continue
  elif reachavg[5] == 'Reach':
    continue
  elif reachavg[5] == ' ':
    continue
  
  else:
    reachlist.append(reachavg[5])

rl = [x for x in reachlist if x != '']
# print(rl)
reachlist = list(map(int, rl)) 
# reachlist = [int(i) for i in reachlist] 

ravg = sum(reachlist) / len(reachlist)
rreachavg = round(ravg)
#print('')
#print("Avg. Reach: ", rreachavg)
########################## this calculates the average of the column - reach 
# print('')
# print(fighterID_one + " " + roster[0][5] + ": " + freach_one)
# print(fighterID_two + " " + roster[0][5] + ": " + freach_two)
# ################## prints out their reaches


# # compare fighter reach and call victory
# print('')
# if freach_one > freach_two:
#   print(fighterID_one + ' has a Reach Advantage!') 
# else: 
#   print(fighterID_two + ' has a Reach Advantage!')