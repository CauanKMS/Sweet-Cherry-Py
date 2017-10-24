#lista = ['abacate', 'coisa'] #so um kickstart

#print(lista)

#lista.sort(key=len)

#print(lista)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")

bsObj = BeautifulSoup(html.read(), 'html.parser')

print(bsObj.span.string)

