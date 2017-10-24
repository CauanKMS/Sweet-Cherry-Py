#verificando filmes em cartaz

from bs4 import BeautifulSoup
import requests

url = "https://www.cinemark.com.br/sao-jose-dos-campos/filmes/em-cartaz?pagina="

filmes = []

for c in (1, 2): #string.ascii_uppercase:
    url = url + str(c)

    page = requests.get(url)

    sopa = BeautifulSoup(page.content, 'html.parser')

    for movie in sopa.findAll('a', {'class': 'movie-image'}):
        print(movie['title'][6:])







# No hope above
    #titles = sopa.find('div', {'class': 'movie-container'})




    #titles = sopa.find('a', {'title': 'movie-container'})

    #nomes = [x.string for x in titles.findAll('a')]

    #filmes.extend(nomes)

#filmes.sort()

#print(' '.join(filmes))