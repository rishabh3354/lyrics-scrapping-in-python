#web scrapping code made by Rishabh Bhardwaj
# follow me at http://www.knoobypie.com/about-me/
# folow me on linkedin @https://www.linkedin.com/in/rishabh-bhardwaj-791903171/
# github https://github.com/rishabh3354

# <<<<<<<<-pre-requestie->>>>>>>>>>>>>>>>
# install the following python module:
# pip install requests
# pip install bs4

# output will be in html format, Recommended to save file in html format

import requests
from bs4 import BeautifulSoup
import os
import re

#make sure you have internet connection

query = input("Search any song you like\n")
url = "https://search.azlyrics.com/search.php?q=" + query
response = requests.get(url)

data = response.text
soup = BeautifulSoup(data, 'lxml')
tags = soup.find_all('a')

l2 = []
for x in tags:
    l2.append(x.get('href'))
l3 = []
for y in l2:
    if "www.azlyrics.com/lyrics/" in y:
        l3.append(y)
count = 1

for i in l3:
    res = i.rstrip('.html')
    res1 = res.split('/')
    print("#" + str(count) + " SONG= " + res1[5] + "      " + "ARTIST= " + res1[4])
    count += 1
count -= 1
if count == 0:
    print("Lyrics not found for " + query)
else:

    print("<<<<<<<<<<<<<< Showing Top" + str(count) + " Results >>>>>>>>>>>>>\n")

    choice = int(input("enter the song number\n"))
    choice -= 1
    if choice <= count-1:

        req = requests.get(l3[choice])

        soup = BeautifulSoup(req.content, "lxml")
        mm = str(soup)

        c = mm.count("<div>")
        pos = 0

        while c > 0:
            startpos = mm.find('<div>', pos, len(mm))
            endpos = mm.find('</div>', startpos, len(mm))
            startpos = startpos + 5
            mydata = mm[startpos:endpos]
            pos = endpos
            c -= 1
        print(mydata)

        # <<<<<<<<<<<=this part is optional if you want to save data in html file  ->>>>>>>>>>>>>>
        # comment below line if you dont want to save data in html file

        fvar = open(r'C:\Users\risha\PycharmProjects\myproject\abc.html', 'w')
        fvar.writelines(mydata)
        fvar.close()

        # <<<<<<<<<<<<<<<-os.system will open abc.html file into a browser ->>>>>>>>>>>>>>>>>>>>
        # comment below line if you dont want to open file in a browser
        os.system(r'C:\Users\risha\PycharmProjects\myproject\abc.html')
    else:
        print("invalid choice")
