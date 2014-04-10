from bs4 import BeautifulSoup

import requests

import sys

r  = requests.get("http://evamsharma.finosus.com/beatles/index.html")

data = r.text

soup = BeautifulSoup(data)
counter = 0  
for table in soup.find_all('table'):
    for row in soup.find_all('tr'):
        '''
        try:
            td = row.find_all('td')[0]
        except IndexError:
            continue
        for link in td.find_all(["a","p"]):
            title = str(link.contents)
            title = list(title)
            i = 0
            while i <= 2:
                del title[0]
                i += 1
            i = 0
            while i <= 1:
                del title[-1]
                i += 1
            title = ''.join(title)
            print(title)
        '''
        try:
            tdyear = row.find_all('td')[1] #what?
        except IndexError:
            print("whoops darn!")
            continue
        for link in tdyear.find_all(["a","p"]):
            year = str(link.contents)
            print(year)
            year = list(year)
            year = ''.join(year)
            print(year)
        
