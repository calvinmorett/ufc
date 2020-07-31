import csv
from collections import Counter 
from heapq import nlargest
import numpy as np
import matplotlib.pyplot as plt

########## Should scrub empty keys in dictionary, even nested dictionaries... Which this turns into after sorting
def tlc_scrub(noluv):
  if type(noluv) is dict:
    return dict((lefteye, tlc_scrub(kandi)) for lefteye, kandi in noluv.items() if kandi and tlc_scrub(kandi))
  else:
    return noluv

def wlr(winloss):
  wl = winloss.split("-")
  wl = list(wl)
  wl = int(wl[0])/int(wl[1])
  ratio = round(wl,2)
  return ratio

keys = []
values = []
def cleaningcrew(diction):
  return {k: v for k, v in diction.items() if k is None}
############################################################ Main Function to extrapolate the frequency of the items inside columns
def average_fighter(index):

  record_words = []
  with open('stats.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next_reader = next(reader)
    col_name = next_reader[index]
    print('\n--------------------------\nSorted Freq for Top ' + col_name + ':\n--------------------------')
    for row in reader:
      csv_words = row[index].split(" ")
      for i in csv_words:
        record_words.append(i)

  avglist_record = []
  for i in record_words:
    x = record_words.count(i)
    avglist_record.append((i,x))
    
  averages_unique_record = dict(set(avglist_record)) # cast it as a dictionary to use .get() method

  aur_empty = cleaningcrew(averages_unique_record)
  items = aur_empty.items()
  for item in items:
    keys.append(item[0])
    values.append(item[1])

  # aur = sorted(averages_unique_record, key=averages_unique_record.get, reverse=True)
  
  aur_scrubed = tlc_scrub(averages_unique_record)
  aur = nlargest(5, aur_scrubed, key = aur_scrubed.get) 

  for val in aur:
    print(val, ":", averages_unique_record.get(val)) 

############################################################ 
# specify a single average category
def statcomp(x):
  average_fighter(x)

############################################################ Because I'm Lazy 
lazy_function = 2

while lazy_function <= 15:
 average_fighter(lazy_function)
 lazy_function += 1
 if lazy_function == 16:
   print('\n--------------------------\nAll Top Stats Defined.')

############################################################ 
# ['cap-date', 'name', 'record', 'height', 'weight', 'reach', 'stance', 'dob', 
#       0         1       2         3         4         5         6      7    
#'slpm', 'stracc', 'sapm', 'strdef', 'tdavg', 'tdacc', 'tddef', 'subavg', '']
#   8        9        10       11        12      13       14        15
############################################################ 
