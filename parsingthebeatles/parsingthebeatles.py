import urllib
import json
import csv
resp = urllib.urlopen('https://raw.githubusercontent.com/evamvid/scrapingthebeatles/master/beatles.json').read()
r=json.loads(resp)
with open('stack.csv', 'wb') as csvfile:
  for x in range(1,309):
      if r[str(x)]['album'] == "Sgt. Pepper's Lonely Hearts Club Band":
          print r[str(x)]['title']
          songwriter = csv.writer(csvfile, delimiter='#', quotechar='"', quoting=csv.QUOTE_NONE)
          songwriter.writerow([r[str(x)]['title']," " + r[str(x)]['album']])
