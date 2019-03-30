from urllib.request import Request, urlopen
import re

#get page data as string
req = Request('https://theporndude.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page = webpage.decode("utf8")

#initialize parsing variables
pagelen = len(page)
start = 0

f = open('pornblocker.txt','w')

while (start != -1):
    i = page.find("href=\"http",start+1)
    if (i > 0):
        linkstart = i + 6
        linkend = page.find("/",linkstart+10)
        f.write(page[linkstart:linkend+1] + "\n")
    start = i

f.close()
