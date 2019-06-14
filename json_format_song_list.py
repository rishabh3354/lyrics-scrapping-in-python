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
import sys

query = sys.argv[1:]
query_str = " ".join(query)
# query_str = input("enter song name\n")

url = "https://search.azlyrics.com/search.php?q=" + query_str

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

try:
    response = requests.get(url, timeout=10, headers=headers)


except requests.ConnectionError as err:
    print("<<<<<< PLEASE CHECK YOUR INTERNET CONNECTION >>>>")
except requests.Timeout as err:
    print("OOPS!! Timeout Error")
except requests.RequestException as err:
    print("OOPS!! UNEXPECTED Error")

else:

    data = response.text

    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find_all('a')

    l2 = []
    for x in tags:
        l2.append(x.get('href'))
    song_url = []
    for y in l2:
        if "www.azlyrics.com/lyrics/" in y:
            song_url.append(y)

    # print(song_url)   # links
    song_title=[]
    song_id=[]
    artist_name=[]

    if len(song_url)!=0:

        for i in song_url:
            res = i.rstrip('.html')
            res1 = res.split('/')
            song_title.append(res1[5])
            artist_name.append(res1[4])
        # print(song_title,artist_name)

        finaldata = []
        dictdata = {}

        for counter in range(0, len(song_url)):
            dictdata['song_id'] = str(counter)
            dictdata['song_name'] = str(song_title[counter])
            dictdata['song_artist'] = str(artist_name[counter])
            dictdata['song_url'] = str(song_url[counter])
            finaldata.append(dictdata.copy())
        print(finaldata)
        sys.stdout.flush()

    else:
        print("Lyrics not found")

