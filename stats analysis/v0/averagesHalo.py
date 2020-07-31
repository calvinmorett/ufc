

import csv
from collections import Counter 
from heapq import nlargest
from halo import Halo

spinner = Halo(text='Loading', text_color='white', spinner='pong')
spinner.start()

########## Should scrub empty keys in dictionary, even nested dictionaries... Which this turns into after sorting
def tlc_scrub(noluv):
    if type(noluv) is dict:
        return dict((lefteye, tlc_scrub(kandi)) for lefteye, kandi in noluv.items() if kandi and tlc_scrub(kandi))
    else:
        return noluv

############################################################ Main Function to extrapolate the frequency of the items inside columns
def average_fighter(index):
  record_words = []
  with open('purestats2.csv', 'r') as csvfile:
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
  # aur = sorted(averages_unique_record, key=averages_unique_record.get, reverse=True)
  aur_scrubed = tlc_scrub(averages_unique_record)
  aur = nlargest(5, aur_scrubed, key = aur_scrubed.get) 

  for val in aur:
    spinner.clear()
    print(val, ":", averages_unique_record.get(val)) 

############################################################ Because I'm Lazy 
lazy_function = 3

while lazy_function <= 15:
  average_fighter(lazy_function)
  lazy_function += 1
  if lazy_function == 16:
    print('\n--------------------------\nAll Top Stats Defined.')

spinner.stop()