from bs4 import BeautifulSoup
import string
import requests

url = "https://www.bayerpet.com.br/Caes/lista-nomes/"

dogs = []

for c in string.ascii_uppercase:
    for k in (1, 2, 3):
        url = url + c + "/" + str(k)

        page = requests.get(url)

        sopa = BeautifulSoup(page.content, 'html.parser')

        dog = sopa.find('ul', {'class': 'list listNames'})

        nomes = [x.string for x in dog.findAll('li')]

        dogs.extend(nomes)

dogs.sort()

print(' '.join(dogs))

    #for page in dogs:
        #print(page.string, page['li'])

    #print(c)

#print(primeiraL)