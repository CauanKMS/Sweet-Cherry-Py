from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://sismpconsultapublica.mpsp.mp.br/ConsultarDistribuicao/ObterFiltrosPorMembro")

bsObj = BeautifulSoup(html.read(), 'html.parser')

#for i in bsObj.option:



listaProcs = bsObj.findAll("option")

for html in listaProcs[1:-5]:
    print(html.string, html['value'])

print(len(listaProcs[1:-5]))

#listaProcsSP = listaProcs[0:-5]

#print(listaProcs)