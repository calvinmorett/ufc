############### this is basically a recall / search function for our csv file - containing a roster of active and inactive ufc fighters and stats. 
############### use their names, in this case Calvin Katter, at index 1526 to display their row of stats.
############### now lets use this functionality to pull in to fighters and bring their stats vs each other.
 
import csv
import matplotlib.pyplot as plt
import numpy as np
import PIL, os, glob
from PIL import Image
from math import ceil, floor

#fighterID_one = input('Fighter Name:  ').title()

fx = fighterID_one = 'Anderson Silva'
fy = fighterID_two = 'Nick Diaz'
fight = [fx, fy]
print(fight)
#stats check
print('---------------------')
def find_index(input): 
    o = open('stats.csv', 'r') 
    ufcroster = csv.reader(o) 
    index = 0 
    for row in ufcroster:
      #print row
      if row[1] == input: 
        return index 
      else : index+=1

f1 = find_index(fighterID_one)
f2 = find_index(fighterID_two)
print(f1,f2)

file = open("stats.csv")
reader = csv.reader(file)

# Iterate over ufc roster
roster = []
for row in reader:
    roster.append(row)

indexloop = 2
header = roster[0][indexloop]

def strips(fnum_statlist):
    s = [b.strip('%') for b in fnum_statlist]
    s = [b.strip('"') for b in s]
    s = [int(float(k)) for k in s]
    return s

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

def wlr(winloss):
  wl = winloss.split("-")
  wl = list(wl)
  wl = int(wl[0])/int(wl[1])
  ratio = round(wl,2)
  return ratio
  
#skip stance and dob
while indexloop <= 15:
  if indexloop == 2:
    f1h = wlr(roster[f1][indexloop])
    f2h = wlr(roster[f2][indexloop])
    if f1h > f2h:
      print('Win Loss Ratio ',f1h, ' over ',f2h)
    elif f1h == f2h:
      print('Win Loss Ratio, Equal ratio')
    else:
      print('Win Loss Ratio ',f2h,' over ', f1h)
    f = str(f1h)
    t = str(f2h)
    csvheader = roster[0][indexloop]
    statcomp()
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

    print(f1statlist)
    print(f2statlist)

    f1plot = strips(f1statlist)
    f2plot = strips(f2statlist)
    #f1plot = [b.strip('%') for b in f1statlist]
    #print(f1plot)
    #for i in range(0, len(f1plot)): 
    #  f1plot[i] = int(float(f1plot[i])) 
	
    #f1plot = [b.strip("'") for b in f1statlist]
    #f1plot = [b.strip("'") for b in f1plot]
    #print(f1plot)
    #f1plot = [int(k) for k in f1plot]

    #f2plot = [b.strip('%') for b in f2statlist]
    print(f1plot,f2plot)
    #for i in range(0, len(f2plot)): 
    #  f2plot[i] = int(float(f2plot[i])) 
	  
    #f2plot = [b.strip("'") for b in f2statlist]
    #f2plot = [b.strip("'") for b in f2plot]
    #f2plot = [int(k) for k in f2plot]
    
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

def plotstats(indexkey):
  fig, ax = plt.subplots()
  plt.use_sticky_edges = True

  labels = fx, fy
  ax.bar(labels, compvalues, align='center', width=0.4, color=['red', 'blue'], edgecolor='black')

  plt.suptitle(complabels, fontsize=14, fontweight='bold')
  plt.ylabel(complabels)
  #plt.title('Fighter Stat Comparison (Per 15m)')

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
  
  #frame = 0
  # should use for loop
  #while frame < 11:
    #filename = 'fighter/fstats'+str(frame)+'.png'
    #plt.savefig(filename, dpi=96)
    #plt.gca()
    #plt.clf()
    #frame += 1
  savefile = 'fighter/fstats'+str(indexkey)+'.png'
  plt.savefig(savefile, dpi=125)
	
def keyup():
  global indexkey
  indexkey = 0
  while indexkey <= 11:
    compstats(indexkey)
    plotstats(indexkey)
    indexkey += 1

keyup()

#Create a Grid/Matrix of Images
PATH = r"fighter/"

frame_width = 1228
images_per_row = 3
padding = 0

os.chdir(PATH)

images = glob.glob("*.png")
images = images[:30]                #get the first 30 images

img_width, img_height = Image.open(images[0]).size
sf = (frame_width-(images_per_row-1)*padding)/(images_per_row*img_width)       #scaling factor
scaled_img_width = ceil(img_width*sf)                   #s
scaled_img_height = ceil(img_height*sf)

number_of_rows = ceil(len(images)/images_per_row)
frame_height = ceil(sf*img_height*number_of_rows) 

new_im = Image.new('RGB', (frame_width, frame_height))

i,j=0,0
for num, im in enumerate(images):
    if num%images_per_row==0:
        i=0
    im = Image.open(im)
    #Here I resize my opened image, so it is no bigger than 100,100
    im.thumbnail((scaled_img_width,scaled_img_height))
    #Iterate through a 4 by 4 grid with 100 spacing, to place my image
    y_cord = (j//images_per_row)*scaled_img_height
    new_im.paste(im, (i,y_cord))
    print(i, y_cord)
    i=(i+scaled_img_width)+padding
    j+=1

new_im.show()
new_im.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)