############### this is basically a recall / search function for our csv file - containing a roster of active and inactive ufc fighters and stats. 
############### use their names, in this case Calvin Katter, at index 1526 to display their row of stats.
############### now lets use this functionality to pull in to fighters and bring their stats vs each other.
 
import csv
import matplotlib.pyplot as plt
import numpy as np

#fighterID_one = input('Fighter Name:  ').title()
print("silva vs diaz")
fx = fighterID_one = 'Anderson Silva'
fy = fighterID_two = 'Nick Diaz'
fight = [fx, fy]
#stats check
print('---------------------')
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

file = open("purestats2.csv")
reader = csv.reader(file)

# Iterate over ufc roster
roster = []
for row in reader:
    roster.append(row)

indexloop = 3
header = roster[0][indexloop]

# f = f1sstring values etc
# t = f2string values etc...
statheaders = []
f1statlist = []
f2statlist = []
def statcomp():
  statheaders.append(csvheader)
  f1statlist.append(f)
  f2statlist.append(t)

# Defining the `calc_height` variable.
def calc_height(raw_height):
# Calculates height from feet-inches to inches
  height_components = raw_height.split("-")
  n_feet = int(height_components[0])
  n_inches = int(height_components[1])

  return (n_feet * 12) + n_inches

#skip stance and dob
while indexloop <= 15:
  if indexloop == 3:
    f1h = calc_height(roster[f1][indexloop])
    f = str(f1h)
    f2h = calc_height(roster[f2][indexloop])
    t = str(f2h)
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 4:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 5:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 8:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 9:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 10:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 11:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 12:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 13:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 14:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
  if indexloop == 15:
    f = roster[f1][indexloop]
    t = roster[f2][indexloop]
    csvheader = roster[0][indexloop]
    statcomp()
    statlabels = [x.strip('"') for x in statheaders]

    # print(f1statlist)
    # print(f2statlist)

    f1plot = [b.strip('"') for b in f1statlist]
    f1plot = [b.strip('"') for b in f1plot]
    f1plot = [b.strip('%') for b in f1plot]
    f1plot = [int(float(k)) for k in f1plot]

    f2plot = [b.strip('"') for b in f2statlist]
    f2plot = [b.strip('"') for b in f2plot]
    f2plot = [b.strip('%') for b in f2plot]
    f2plot = [int(float(k)) for k in f2plot]
    
    print(f1plot)
    print(f2plot)
    plotzip = zip(f1plot, f2plot)
    f1vsf2 = list(plotzip)
    print(f1vsf2)
    #print(statlabels,statplot)
  indexloop += 1

# use zip among 2 lists to create a list of tuples for matplotlib to use as values
# f1statlist = [1,2,3]
# f2statlist = [x,y,z]

def compstats(index):
  global compvalues
  global complabels
  compvalues = f1vsf2[index]
  complabels = statlabels[index]

def plotstats():
  fig, ax = plt.subplots()
  plt.use_sticky_edges = True

  labels = fx, fy
  ax.bar(labels, compvalues, align='center', width=0.4, color=['red', 'green'], edgecolor='black')

  plt.ylabel(complabels)
  plt.title('Fighter Stat Comparison [Per 15m]')

  # set the style of the axes and the text color
  plt.rcParams['axes.edgecolor']='#333F4B'
  plt.rcParams['axes.linewidth']=0.8
  plt.rcParams['xtick.color']='#333F4B'
  plt.rcParams['ytick.color']='#333F4B'
  plt.rcParams['text.color']='#333F4B'
  # change the style of the axis spines
  ax.spines['top'].set_color('none')
  ax.spines['right'].set_color('none')

  # set the spines position
  ax.spines['bottom'].set_position(('axes', 0))
  ax.spines['left'].set_position(('axes', 0))

  plt.show()

def keyup():
  indexkey = 0
  while indexkey <= 10:
    compstats(indexkey)
    plotstats()
    indexkey += 1

keyup()