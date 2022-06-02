import requests
from bs4 import BeautifulSoup
import sys


query_str = "alan walker"
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