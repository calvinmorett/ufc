from bs4 import BeautifulSoup as bs
# import csv
import re
import requests
from datetime import datetime
import time

# A's - urlist = ['http://ufcstats.com/fighter-details/93fe7332d16c6ad9', 'http://ufcstats.com/fighter-details/15df64c02b6b0fde', 'http://ufcstats.com/fighter-details/b361180739bed4b0', 'http://ufcstats.com/fighter-details/2f5cbecbbe18bac4', 'http://ufcstats.com/fighter-details/c0ed7b208197e8de', 'http://ufcstats.com/fighter-details/5140122c3eecd307', 'http://ufcstats.com/fighter-details/c9f6385af6df66d7', 'http://ufcstats.com/fighter-details/aa6e591c2a2cdecd', 'http://ufcstats.com/fighter-details/7279654c7674cd24', 'http://ufcstats.com/fighter-details/1c5879330d42255f', 'http://ufcstats.com/fighter-details/2620f3eb21c79614', 'http://ufcstats.com/fighter-details/83b00f7597e5ac83', 'http://ufcstats.com/fighter-details/a77633a989013265', 'http://ufcstats.com/fighter-details/79cb2a690b9ba5e8', 'http://ufcstats.com/fighter-details/1338e2c7480bdf9e', 'http://ufcstats.com/fighter-details/0e9869d712e81f8f', 'http://ufcstats.com/fighter-details/ebc5af72ad5a28cb', 'http://ufcstats.com/fighter-details/a08ddd04eaffd81d', 'http://ufcstats.com/fighter-details/44aa652b181bcf68', 'http://ufcstats.com/fighter-details/6cadc0a0ba7dc015', 'http://ufcstats.com/fighter-details/8f382b3baa954d2a', 'http://ufcstats.com/fighter-details/cf946e03ba2e7666', 'http://ufcstats.com/fighter-details/ae071698e1a3ccd4', 'http://ufcstats.com/fighter-details/9e3dbb9c68ed5d1a', 'http://ufcstats.com/fighter-details/2eada40ac8801559', 'http://ufcstats.com/fighter-details/16690d100f995f8f', 'http://ufcstats.com/fighter-details/b0550072e5f0afa7', 'http://ufcstats.com/fighter-details/1fc64507a0cb38cf', 'http://ufcstats.com/fighter-details/38b50fd1e1b5b656', 'http://ufcstats.com/fighter-details/1cf1310684a841f5', 'http://ufcstats.com/fighter-details/7578cc6bd750206b', 'http://ufcstats.com/fighter-details/2144954270be834d', 'http://ufcstats.com/fighter-details/1897b7b913736a7c', 'http://ufcstats.com/fighter-details/9b28292abe3166d5', 'http://ufcstats.com/fighter-details/7bd94b60d7521e4a', 'http://ufcstats.com/fighter-details/c482c8605455a213', 'http://ufcstats.com/fighter-details/184b955181bdef52', 'http://ufcstats.com/fighter-details/e76d9f656ceb82ab', 'http://ufcstats.com/fighter-details/dd1b90eea08887f6', 'http://ufcstats.com/fighter-details/39f62b833e4cf126', 'http://ufcstats.com/fighter-details/2f95a3c6d58b2aad', 'http://ufcstats.com/fighter-details/7c6e87729e824ef4', 'http://ufcstats.com/fighter-details/1e38bba6738b7b10', 'http://ufcstats.com/fighter-details/d26934530dc5b248', 'http://ufcstats.com/fighter-details/578ef12674df1e6a', 'http://ufcstats.com/fighter-details/c487223b0289bda9', 'http://ufcstats.com/fighter-details/d0f3959b4a9747e6', 'http://ufcstats.com/fighter-details/6fd953151d981979', 'http://ufcstats.com/fighter-details/fe5a9547479396ab', 'http://ufcstats.com/fighter-details/7a15f3694c5cbc02', 'http://ufcstats.com/fighter-details/0541480fbf719d86', 'http://ufcstats.com/fighter-details/8fd76e1b49c00ae2', 'http://ufcstats.com/fighter-details/d53482bef23235ba', 'http://ufcstats.com/fighter-details/b757c73f443d4fca', 'http://ufcstats.com/fighter-details/4b37a0bc2ab4cae1', 'http://ufcstats.com/fighter-details/41b34b7f11f6d085', 'http://ufcstats.com/fighter-details/9abc648e76c4493a', 'http://ufcstats.com/fighter-details/669a3cb6e394f515', 'http://ufcstats.com/fighter-details/e17770faae3ca54c', 'http://ufcstats.com/fighter-details/e70de1859b7ee78e', 'http://ufcstats.com/fighter-details/6ebe96a116e79e52', 'http://ufcstats.com/fighter-details/1e13936d708bcff7', 'http://ufcstats.com/fighter-details/040a74bb0a465c54', 'http://ufcstats.com/fighter-details/2f181c0467965b98', 'http://ufcstats.com/fighter-details/c4fe2e9a06ea5bcb', 'http://ufcstats.com/fighter-details/91186547a7f3f758', 'http://ufcstats.com/fighter-details/d615d6a10a4704cd', 'http://ufcstats.com/fighter-details/2b074403b7c6cdb4', 'http://ufcstats.com/fighter-details/67a992d4cff22466', 'http://ufcstats.com/fighter-details/f16ddfa31236efed', 'http://ufcstats.com/fighter-details/c6bf75775b278ed8', 'http://ufcstats.com/fighter-details/49b130de1da2e1bf', 'http://ufcstats.com/fighter-details/c61b49cec6abd6b9', 'http://ufcstats.com/fighter-details/c11036da9162cb5f', 'http://ufcstats.com/fighter-details/e741536153227386', 'http://ufcstats.com/fighter-details/33a331684283900f', 'http://ufcstats.com/fighter-details/4438482bd1d5a029', 'http://ufcstats.com/fighter-details/58bbef3770bb2dfc', 'http://ufcstats.com/fighter-details/31ee470ef5dc8d7f', 'http://ufcstats.com/fighter-details/bd92cf5da5413d2a', 'http://ufcstats.com/fighter-details/dc5a6b2fdb27e7dc', 'http://ufcstats.com/fighter-details/d317a5e2b3f88c5f', 'http://ufcstats.com/fighter-details/d156513a19acf856', 'http://ufcstats.com/fighter-details/20821819c401ced8', 'http://ufcstats.com/fighter-details/1e327b281ef6a745', 'http://ufcstats.com/fighter-details/247fbbfafea60bb1', 'http://ufcstats.com/fighter-details/ee0b69e307c857e5', 'http://ufcstats.com/fighter-details/c912f676692c353a', 'http://ufcstats.com/fighter-details/d562b12b8fe88336', 'http://ufcstats.com/fighter-details/70fa1c64a2c439ef', 'http://ufcstats.com/fighter-details/87a1dc546b1c5caf', 'http://ufcstats.com/fighter-details/53adf5b845d91e4a', 'http://ufcstats.com/fighter-details/23a8c33869bf5392', 'http://ufcstats.com/fighter-details/cad24459b28592ca', 'http://ufcstats.com/fighter-details/8738eacd62e82a32', 'http://ufcstats.com/fighter-details/9199e0735b83dd32', 'http://ufcstats.com/fighter-details/1ffc38f67785797b', 'http://ufcstats.com/fighter-details/5e4eec08896c9423', 'http://ufcstats.com/fighter-details/19ba965651486013', 'http://ufcstats.com/fighter-details/a0e75f4a13eb73f1', 'http://ufcstats.com/fighter-details/1562b12763cc8d67', 'http://ufcstats.com/fighter-details/6a1901c62ab3870f', 'http://ufcstats.com/fighter-details/d221ee27afc7a60e', 'http://ufcstats.com/fighter-details/9bad58fa651d6196', 'http://ufcstats.com/fighter-details/00debc804e2b1cd4', 'http://ufcstats.com/fighter-details/46e2ca71fd5089cb', 'http://ufcstats.com/fighter-details/e20ad078a7d63361', 'http://ufcstats.com/fighter-details/e06fd1260ac865a7', 'http://ufcstats.com/fighter-details/d802174b0c0c1f4e', 'http://ufcstats.com/fighter-details/d343df8ba11f4c4e', 'http://ufcstats.com/fighter-details/af997f7611673880', 'http://ufcstats.com/fighter-details/25b31165758402dd', 'http://ufcstats.com/fighter-details/dbd198f780286aca', 'http://ufcstats.com/fighter-details/78d48d3874dacafd', 'http://ufcstats.com/fighter-details/4665f9f909cd7214', 'http://ufcstats.com/fighter-details/79ded75550efc139', 'http://ufcstats.com/fighter-details/0c1a04afca64e38f', 'http://ufcstats.com/fighter-details/1ccff7f0cfdf85eb', 'http://ufcstats.com/fighter-details/269d103c96a4c3a5', 'http://ufcstats.com/fighter-details/73ef22f25d0f70e2', 'http://ufcstats.com/fighter-details/71002dbc1743b9a7', 'http://ufcstats.com/fighter-details/dbea8c1cb327ab3d', 'http://ufcstats.com/fighter-details/36541f1e6c5d4955', 'http://ufcstats.com/fighter-details/1291edf2d566a71a', 'http://ufcstats.com/fighter-details/d25e39e74efb0a77', 'http://ufcstats.com/fighter-details/9c9455912d917e4e', 'http://ufcstats.com/fighter-details/3738e68d2261e60f', 'http://ufcstats.com/fighter-details/30ad2050273d016a', 'http://ufcstats.com/fighter-details/bf0e700106d00e55', 'http://ufcstats.com/fighter-details/05fbfe628658c538', 'http://ufcstats.com/fighter-details/770b9d4813c25902', 'http://ufcstats.com/fighter-details/c136b2a8852da5bd', 'http://ufcstats.com/fighter-details/de62052b2ede65ba', 'http://ufcstats.com/fighter-details/61fb8098ccf81c7f', 'http://ufcstats.com/fighter-details/2dea80c069847321', 'http://ufcstats.com/fighter-details/91e3388e69060e69', 'http://ufcstats.com/fighter-details/49f78022126bf4a4', 'http://ufcstats.com/fighter-details/a373085066dbfb54', 'http://ufcstats.com/fighter-details/b1d19449397541dc', 'http://ufcstats.com/fighter-details/9be6020024133293', 'http://ufcstats.com/fighter-details/06827d70c53ff0d9', 'http://ufcstats.com/fighter-details/0b31f87be71ebbb1', 'http://ufcstats.com/fighter-details/399afbabc02376b5', 'http://ufcstats.com/fighter-details/ff222167cce02919', 'http://ufcstats.com/fighter-details/d0d7160824278840', 'http://ufcstats.com/fighter-details/2f13e4020cea5b38', 'http://ufcstats.com/fighter-details/fd7acf42bd6e7e95', 'http://ufcstats.com/fighter-details/210935fd21670f6d', 'http://ufcstats.com/fighter-details/55ee431411ccf07a', 'http://ufcstats.com/fighter-details/196ed28337adc630', 'http://ufcstats.com/fighter-details/04643fd03d9159cc', 'http://ufcstats.com/fighter-details/956dcac65e7b34d6', 'http://ufcstats.com/fighter-details/8753e125f4499816', 'http://ufcstats.com/fighter-details/ba5c6eeb8ef45f5c', 'http://ufcstats.com/fighter-details/033d19259f589457', 'http://ufcstats.com/fighter-details/4665cbf36b08193b', 'http://ufcstats.com/fighter-details/86d9dbe1bfcbade7', 'http://ufcstats.com/fighter-details/da603332ad41f165', 'http://ufcstats.com/fighter-details/26387c19f32dda0f', 'http://ufcstats.com/fighter-details/6eaec40f724852f4', 'http://ufcstats.com/fighter-details/46d0a888d87d91ac', 'http://ufcstats.com/fighter-details/ee18ff42063174df', 'http://ufcstats.com/fighter-details/063649e21bc9d6d5', 'http://ufcstats.com/fighter-details/9bcfb40dbcd50568', 'http://ufcstats.com/fighter-details/2af2f2e26c4c0402']
# Z's urlist = ['http://ufcstats.com/fighter-details/2284092f8b63273b', 'http://ufcstats.com/fighter-details/8c822811eedc11ad', 'http://ufcstats.com/fighter-details/24656ef4d605c96f', 'http://ufcstats.com/fighter-details/52c2ae6d2f2d2613', 'http://ufcstats.com/fighter-details/8adcbd525fab8d9b', 'http://ufcstats.com/fighter-details/cc3878d1ab41a5fa', 'http://ufcstats.com/fighter-details/fe5ca7ef93c3f6a7', 'http://ufcstats.com/fighter-details/abcf7e55a0a9ed89', 'http://ufcstats.com/fighter-details/3bb2dc8e87b10a46', 'http://ufcstats.com/fighter-details/be4076c9e8d791e3', 'http://ufcstats.com/fighter-details/3794e5e0bb0defb6', 'http://ufcstats.com/fighter-details/3144121470023e9a', 'http://ufcstats.com/fighter-details/cbf69fa846c7e3ee', 'http://ufcstats.com/fighter-details/55fa6ce3e522c8bb', 'http://ufcstats.com/fighter-details/c23e3d4875340d8d', 'http://ufcstats.com/fighter-details/7b310409440c9102', 'http://ufcstats.com/fighter-details/1ebe20ebbfa15e29', 'http://ufcstats.com/fighter-details/5ea918ea81b7dee2', 'http://ufcstats.com/fighter-details/1e4f273069fb9e85', 'http://ufcstats.com/fighter-details/6d3398b910461f2f', 'http://ufcstats.com/fighter-details/4b4fc3ddc307bc73', 'http://ufcstats.com/fighter-details/0aa74d04c196800c', 'http://ufcstats.com/fighter-details/3ecd936bd8814108', 'http://ufcstats.com/fighter-details/108afe61a26bcbf4', 'http://ufcstats.com/fighter-details/be124bdd60fab7d5']

# O's urlist =  ['http://ufcstats.com/fighter-details/20bcc9966affb19c', 'http://ufcstats.com/fighter-details/d25b93992f285953', 'http://ufcstats.com/fighter-details/cb52f9490c2dc069', 'http://ufcstats.com/fighter-details/69ea0119f6f0dfe0', 'http://ufcstats.com/fighter-details/46effbd1135423c5', 'http://ufcstats.com/fighter-details/b50a426a33da0012', 'http://ufcstats.com/fighter-details/338fda4ec7034c5d', 'http://ufcstats.com/fighter-details/56bc9ccb609df534', 'http://ufcstats.com/fighter-details/494b0bfdbac74502', 'http://ufcstats.com/fighter-details/7139cd2ae4bf6a29', 'http://ufcstats.com/fighter-details/6e3282d57d2467a0', 'http://ufcstats.com/fighter-details/2d6d6ffe5a446ea2', 'http://ufcstats.com/fighter-details/f43907e75f8d9baa', 'http://ufcstats.com/fighter-details/0845c81e37d3bcb3', 'http://ufcstats.com/fighter-details/4b2390cfaceb91d8', 'http://ufcstats.com/fighter-details/b6c4451cb13c9303', 'http://ufcstats.com/fighter-details/6a8a06b542e1516d', 'http://ufcstats.com/fighter-details/01daf32100ed7517', 'http://ufcstats.com/fighter-details/32541eb5d12668b4', 'http://ufcstats.com/fighter-details/acff437707625fc7', 'http://ufcstats.com/fighter-details/aa40fe6038db56cb', 'http://ufcstats.com/fighter-details/33454ad90754cb49', 'http://ufcstats.com/fighter-details/02a65a55f25fb4f3', 'http://ufcstats.com/fighter-details/98c23cb6da5b3352', 'http://ufcstats.com/fighter-details/0d65c432720accb9', 'http://ufcstats.com/fighter-details/15b1b21cd743d652', 'http://ufcstats.com/fighter-details/07225ba28ae309b6', 'http://ufcstats.com/fighter-details/bec2746f033802c3', 'http://ufcstats.com/fighter-details/acd9513399a8b09b', 'http://ufcstats.com/fighter-details/57b10fca4f9c9a7a', 'http://ufcstats.com/fighter-details/32c03df3c9760069', 'http://ufcstats.com/fighter-details/948880beac71f028', 'http://ufcstats.com/fighter-details/e96d8538d3f9d0ed', 'http://ufcstats.com/fighter-details/dfbb95ca0c143988', 'http://ufcstats.com/fighter-details/7613773461b276f4', 'http://ufcstats.com/fighter-details/8e0709784259402d', 'http://ufcstats.com/fighter-details/5a9104718439ef44', 'http://ufcstats.com/fighter-details/f2ad06f1007c481a', 'http://ufcstats.com/fighter-details/470fedbc8563ac47', 'http://ufcstats.com/fighter-details/9f842be1a5337be6', 'http://ufcstats.com/fighter-details/318572f6f74b760d', 'http://ufcstats.com/fighter-details/887e09328cd63df1', 'http://ufcstats.com/fighter-details/6b8db407d49c6e4b', 'http://ufcstats.com/fighter-details/def8166ff24bd237', 'http://ufcstats.com/fighter-details/2f732dd9210d301f', 'http://ufcstats.com/fighter-details/9c5828c6fd9dc948', 'http://ufcstats.com/fighter-details/f53c1f4ceeed8c08', 'http://ufcstats.com/fighter-details/8eb239a52fc4ec14', 'http://ufcstats.com/fighter-details/6d68c1afe954f121', 'http://ufcstats.com/fighter-details/f84dfc5a8d178403', 'http://ufcstats.com/fighter-details/5b407acfe0ef9b76', 'http://ufcstats.com/fighter-details/d632d156c0549e07', 'http://ufcstats.com/fighter-details/01784fbc27c68b14', 'http://ufcstats.com/fighter-details/4512e46543b960ad', 'http://ufcstats.com/fighter-details/865aa315ea62c511', 'http://ufcstats.com/fighter-details/6b8f28da9a483049', 'http://ufcstats.com/fighter-details/47cd337b86b1af92', 'http://ufcstats.com/fighter-details/1ef0eae31904e534', 'http://ufcstats.com/fighter-details/871ce0b4a01922b6', 'http://ufcstats.com/fighter-details/b4ad3a06ee4d660c', 'http://ufcstats.com/fighter-details/20e403a1acfef130', 'http://ufcstats.com/fighter-details/4bb9d7a32d02a03e', 'http://ufcstats.com/fighter-details/47b7e4e60813b7b2', 'http://ufcstats.com/fighter-details/e18a19001a3f7c7d']

urlist = ['http://ufcstats.com/fighter-details/e6dac752a2418a88']


maxurlnum = len(urlist)

letter = input("What Letter are you on?  ")

# print(maxurlnum)  = 165
# if maxurlnum == 0 or < maxurlnum add 1 to the index value of url[0]
# set link batch as that url value replaced/changed

def savestats():
    today = datetime.now()

    uindex = 0
    while uindex <= maxurlnum:
        scrapeurl = urlist[uindex]
        req = requests.get(scrapeurl)
        soup = bs(req.content, 'html.parser')

        addstatstofile = open(letter + 'stats.txt', "a")

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

# =============================== 
# =============================== 
# don't need this printed everytime the function executes
# print(fnts)
# print(rts)

# fighter stats 
# height, weight, reach, stance, dob
# sig strikes per 15m, sig strike accuracy, sig strikes absorbed per minute, sig strikes defense
# avg takedowns per 15m, takedown accuracy, takedown def, sub average

# data.append((title))

#\s - whitespace
# # open a CSV file with append, so old data will not be erased
# with open('index.csv', 'a', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([fnts])
#     writer.writerow([fts])
#     writer.writerow([css])
#     writer.writerow([today])