#Calculando os gastos do Brasa na copa

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")

bsObj = BeautifulSoup(html.read(), 'xml')

obras = bsObj.findAll("valorTotalPrevisto")

total = 0

for v in obras:
    print(v.string)

    total = total + float(v.string)

print(total)

#print(html.read().decode('utf-8'))