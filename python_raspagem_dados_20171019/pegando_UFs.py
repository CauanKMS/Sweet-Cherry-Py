from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://g1.globo.com/educacao/universidades.html")

sopa = BeautifulSoup(html.read(), 'html.parser')

#so pegando a sigla, mas tem mais coisas nisso aqui :)
sigla = [sig.string.strip() for sig in sopa.findAll('td',{'class': 'sigla'})]

print(sigla)