import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

print("Fighting the Stat: Striking Accuracy ")
print('---------------------')

def accurate(): 
    global name
    global record
    global sigacc
    o = open('stats.csv', 'r') 
    reader = csv.reader(o)
    next(reader)
    above45 = []
    name = []
    record = []
    sigacc = []
    index = 0
    rows = [row for row in reader if row[9] > '45']
    for row in rows:
      above45.append(row) # appends every row with an above 45% significant strike accuracy
      name.append(above45[index][1]) # name index
      record.append(above45[index][2]) # record index
      sigacc.append(above45[index][9]) # signifiant strike accuracy index   

      index+=1

accurate()

def wlr(winloss):
  global newrec
  newrec = []
  x = 0
  while x < len(winloss):
    wl = winloss[x].split("-")
    wl = list(wl)
    if wl[1] > '0':      
      wl = int(wl[0])/int(wl[1])
      ratio = round(wl,3)
      newrec.append(ratio) 
      x += 1
    else:
      newrec.append('30')
      x += 1

wlr(record)
#print(newrec)

nrec = [int(i) for i in newrec] 
ssa = [int(i) for i in sigacc] 

df = pd.DataFrame(list(zip(name, nrec, ssa)), 
               columns =['Name', 'WLR', 'Sig. Strike Accuracy']) 
df2 = df[(df['WLR'] > 3)] # conor has a wlr of 5
df3 = df2[(df2['Sig. Strike Accuracy'] > 40)]
df = df3.sort_values('Sig. Strike Accuracy', ascending = True)

# label = 'Juan Espino'

# plt.annotate(label, # this is the text
#                  (95,10), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'GSP'

# plt.annotate(label, # this is the text
#                  (53,13), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Jon Jones'
# plt.annotate(label, # this is the text
#                  (57,26), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Michael Page'
# plt.annotate(label, # this is the text
#                  (76,30), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center
      
# label = 'Paulo Costa'
# plt.annotate(label, # this is the text
#                  (57,30), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Daniel Cormier'
# plt.annotate(label, # this is the text
#                  (52,11), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Conor McGregor'
# plt.annotate(label, # this is the text
#                  (49,4), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  horizontalalignment='right',
#                  verticalalignment='top',
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Anderson Silva'
# plt.annotate(label, # this is the text
#                  (62,3), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  horizontalalignment='right',
#                  verticalalignment='top',
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center     

plt.grid(True)
plt.margins(0.1)
plt.scatter(df['Sig. Strike Accuracy'],df['WLR'])
plt.xlabel('Significant Striking Accuracy', fontsize=15,rotation=1)
plt.ylabel('Win Loss Ratio [30 = Perfect WLR]', fontsize=15)
savefile = 'fight/sigacc.png'
plt.savefig(savefile, dpi=125)


plt.show()
print(df)