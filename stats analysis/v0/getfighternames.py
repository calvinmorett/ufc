import pandas as pd
import csv
#from halo import Halo

df = pd.read_csv('treatx.csv', sep=',',)
#spinner = Halo(text='Loading CSV', spinner='dots')
#spinner.start()
print(' ')
fighterlastname = input('Fighter Last Name:')
print(' ')

for player in df:
    if player[1] == "fighterlastname":
        print(player)

#spinner.stop()






#x = df.loc[df.index[2]]
# #print(x)
# diazlist = []
# for i in df.index:
#     finder = df['name'].str.contains('Diaz')
#     diazlist.extend(finder)  
#     i += 1
#     for diazexists in diazlist:
#         if diazlist == True:
#             print(diazexists)
#         else:
#             continue
    
#     if i == 3432:
#         break

# would select a column called name
# This would show observations which start with STARBUC
# match = df['name'].str.contains('(^Diaz)')
# match .str.extract
# df.to_html('temp.html')


# key = 'Diaz,'
# with pd.read_csv as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     result = [row[1].strip() for row in reader if row[0].strip() == key]

# print(result)