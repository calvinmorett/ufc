from bs4 import BeautifulSoup as bs
import re
import requests
from datetime import datetime
import time
# import pprint
# import csv

today = datetime.now()

# filename = input("Filename:  ")
################ flinkz
################ contains
################ all the links for the fighter stats a-Z....


# req = requests.get(url)

# soup = bs(req.content, 'html.parser')

# links = []
# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#     links.append(link.get('href'))

# all_links = list(dict.fromkeys(links))

# #print(len(all_links)) 

# with open(filename + ".txt", "w") as outfile:
#     outfile.write("\n".join(all_links))
#     outfile.close()

#############################################################
# List conversion section

lisa = open("link-list.txt").readlines()
# if it's already a list, you don't need to convert it to one

homer = [listitem.rstrip() for listitem in lisa]

# print(urlist)
# homer = [listitem.rstrip() for listitem in lisa] \\\\ # # save yourself a step... 

# don't pop or print here, because it's a giant list and this isnt needed.
# homer.pop(0)
# homer.pop(-1)
# homer.pop(-1)
# print(homer)

with open("list.txt", "w") as listconv:
    listconv.write(str(homer))
    listconv.close()

#############################################################
# Web Scraping section

print("\n" + 'Section Initialized' + '\n')

urlist = homer 
# # save yourself a step... 

maxurlnum = len(urlist)
print(maxurlnum)
def savestats():
    today = datetime.now()
    uindex = 0
    while uindex <= maxurlnum:
        scrapeurl = urlist[uindex]
        #index of a list, in a file.
        req = requests.get(scrapeurl)
        soup = bs(req.content, 'html.parser')

        addstatstofile = open("allstats.txt", "a")

        # fighter name - Output: Curtis Blaydes
        for fightername in soup.findAll('span', attrs={'class': 'b-content__title-highlight'}):
            fnts = fightername.text.strip()
    
        # fighter record - Output: Record: 14-2-0 (1 NC)
        for record in soup.findAll('span', attrs={'class': 'b-content__title-record'}):
            rts = record.text.strip()

        addstatstofile.writelines('\n' + str(today) + '\n')
        addstatstofile.writelines(str(fnts) + '\n')
        addstatstofile.writelines(str(rts) + '\n')

        for careerstats in soup.findAll('li', attrs={'class': 'b-list__box-list-item'}):
            csgts = careerstats.get_text().split()
            css = ' '.join(csgts)
            for line in css.splitlines():
                if not line.strip():
                    continue
                else:
                    # you need to add the new line in the text file, the output in console does it for you
                    addstatstofile.writelines(str(line) + '\n')
            
        if uindex == maxurlnum:
            break
        elif maxurlnum + 1 == True:
            break
        else:
            today = datetime.now()
            uindex += 1
    

    print(uindex)
    time.sleep(3)
    savestats()
        
savestats()