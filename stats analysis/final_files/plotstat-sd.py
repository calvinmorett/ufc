import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

print("Fighting the Stat: Strike Defense ")
print('---------------------')

pd.set_option('display.max_rows', None)
############################################################ 
# ['cap-date', 'name', 'record', 'height', 'weight', 'reach', 'stance', 'dob', 
#       0         1       2         3         4         5         6      7    
#'slpm', 'stracc', 'sapm', 'strdef', 'tdavg', 'tdacc', 'tddef', 'subavg', '']
#   8        9        10       11        12      13       14        15
############################################################ 
def accurate(colindex): 
    global name
    global record
    global strdef
    o = open('stats.csv', 'r') 
    reader = csv.reader(o)
    next(reader)
    above45 = []
    name = []
    record = []
    strdef = []
    index = 0
    rows = [row for row in reader if row[colindex] > '60']
    for row in rows:
      above45.append(row) # appends every row with an above 45% significant strike accuracy
      name.append(above45[index][1]) # name index
      record.append(above45[index][2]) # record index
      strdef.append(above45[index][9]) # signifiant strike accuracy index   

      index+=1

accurate(11)


# print(len(name))
# print(len(record))
# print(len(tddef))

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
strdefx = [int(i) for i in strdef] 

df = pd.DataFrame(list(zip(name, nrec, strdefx)), 
               columns =['Name', 'WLR', 'Strike Defense']) 
df2 = df[(df['WLR'] > 3)] # conor has a wlr of 5
df3 = df2[(df2['Strike Defense'] > 40)]
df = df3.sort_values('Strike Defense', ascending = True)

# # 426      Khabib Nurmagomedov   30                  49
# # 429            Sean O'malley   30                  58
# # 289       Demetrious Johnson    9                  54
# # 425             Amanda Nunes    5                  51
# # 562        Georges St-Pierre   13                  53
# # 376           Conor Mcgregor    5                  49
# # 196         Gregor Gillespie   13                  49
# # 10                 Jose Aldo    4                  44
# # 251             Max Holloway    4                  44
# #203          Justin Gonzales   30                  80
# #576              Kevin Syler   30                  75
# #25          Julius Anglickas    5                  78


# 252                Jon Jones   26              57

# 524        Georges St-Pierre   13              53

# # 594                 Petr Yan   14              46

# 378               Tom Murphy   30              71
# 553            Anatoly Tokov   12              72

# 246       Joanna Jedrzejczyk    4              48
label = ' Tom Murphy'
plt.annotate(label, # this is the text
                 (71,30), # this is the point to label 
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
label = 'Anatoly Tokov'
plt.annotate(label, # this is the text
                 (72,12), # this is the point to label 
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
label = 'Jon Jones'
plt.annotate(label, # this is the text
                 (57,26), # this is the point to label 
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

label = 'Georges St-Pierre'
plt.annotate(label, # this is the text
                 (53,13), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
label = 'Petr Yan'
plt.annotate(label, # this is the text
                 (46,14), # this is the point to label 
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

label = 'Joanna Jedrzejczyk '
plt.annotate(label, # this is the text
                 (48,4), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
label = 'Michael Page'
plt.annotate(label, # this is the text
                 (76,30), # this is the point to label 
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

label = 'Neiman Gracie'
plt.annotate(label, # this is the text
                 (100,30), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

label = 'Michael Page'
plt.annotate(label, # this is the text
                 (76,30), # this is the point to label 
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

label = 'Neiman Gracie'
plt.annotate(label, # this is the text
                 (100,30), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center



# tddef

#   # Calvin Kattar    5                 41 
#   # Jon Jones   26                 57

# label = ' Calvin Kattar'
# plt.annotate(label, # this is the text
#                  (41,5), # this is the point to label 
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Jon Jones '
# plt.annotate(label, # this is the text
#                  (57,26), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Justin Gonzales'

# plt.annotate(label, # this is the text
#                  (80,30), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Max Holloway'

# plt.annotate(label, # this is the text
#                  (44,4), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center
#  Israel Adesanya   30                 48
 #         Henry Cejudo    8                 45
# #402            Rene Kronvold    5                100
# label = 'Rene Kronvold'

# plt.annotate(label, # this is the text
#                  (100,5), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Henry Cejudo'

# plt.annotate(label, # this is the text
#                  (45,8), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Conor McGregor'
# plt.annotate(label, # this is the text
#                  (49,5), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Khabib Nurmagomedov'
# plt.annotate(label, # this is the text
#                  (49,30), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center
      
# label = 'GSP'
# plt.annotate(label, # this is the text
#                  (53,13), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Amanda Nunes'
# plt.annotate(label, # this is the text
#                  (51,5), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Demetrious Johnson'
# plt.annotate(label, # this is the text
#                  (54,9), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Sean O-Malley'
# plt.annotate(label, # this is the text
#                  (58,30), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  horizontalalignment='right',
#                  verticalalignment='top',
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# label = 'Khabib Nurmagomedov'
# plt.annotate(label, # this is the text
#                  (49,30), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  horizontalalignment='right',
#                  verticalalignment='top',
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center     

plt.grid(True)
plt.margins(0.1)
plt.scatter(df['Strike Defense'],df['WLR'])
plt.xlabel('Strike Defense', fontsize=15,rotation=1)
plt.ylabel('Win Loss Ratio [30 = Perfect WLR]', fontsize=15)

plt.show()
print(df)