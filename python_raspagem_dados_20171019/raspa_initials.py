#How to open a page and get its HTML

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://beans.itcarlow.ie/prices.html")

#algo = html.read().decode('utf-8')

#print(algo)

bsObj = BeautifulSoup(html.read(), 'html.parser')

print(bsObj.strong)

print(bsObj.strong.string)

#print(chr(33000)) #get an ascii char