from bs4 import BeautifulSoup
import requests, bleach             #external/installed (`pip install requests` and `pip install bleach`)
import pprint, json                 #builtin

r  = requests.get("http://evamsharma.finosus.com/beatles/index.html")

data = r.text

dict = {} #initialize dictionary (probably redundant)

soup = BeautifulSoup(data)
counter = 0  

for table in soup.find_all('table'):
    for row in soup.find_all('tr')[1:]: #for each row from the second on
        try:
            td = row.find_all('td')[0]
        except IndexError:
            continue
        for link in td.find_all(["a","p"]):
            title = str(link.contents)
            title = list(title)
            i = 0
            while i <= 2:             #Loop takes off first 3 characters
                del title[0]          #           
                i += 1                #       
            i = 0                     #  
            while i <= 1:             #Loop takes off last 2 characters  
                del title[-1]         #         
                i += 1                #  
            title = ''.join(title) #list back to string
            title = title.decode('utf-8')
            title.replace(u'\xa9', 'e')
        try:
            tdyear = row.find_all('td')[1] #indexed columns -- this is the second collumn
        except IndexError:
            continue
        year = ''.join(tdyear.contents) #string back to list
        try:
            tdalbum = row.find_all('td')[2] #indexed columns -- this is the third collumn
        except IndexError:
            continue
        #album = "".join(tdalbum.contents)
        album = bleach.clean(tdalbum, tags=[], strip=True) #uses bleach to strip all tags from album
        
        title = title.encode('utf-8')
        year = year.encode('utf-8')
        album = album.encode('utf-8') #encodes in utf-8 so terminal has an easier time with it
        counter += 1 #indexes each song in the dictionary
        dict[counter] = {'title': title, 'year': year, 'album': album} #append all the variables into the dictionary
        #print(title + " " + "(" + year + ")" + " " + "on" + " " + album) #print a nicely formatted "song(year) on album"
#print(json.dumps(dict, indent = 2)) #dump the dictionary to JSON and print
file = open("beatles.json", "w")
file.write(json.dumps(dict, indent = 2))
file.close()
