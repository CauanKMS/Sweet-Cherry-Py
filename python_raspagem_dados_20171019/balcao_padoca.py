#Na vdd esse py aqui eh pra testar uma api pra verificar qtd de escolas com determinadas coisas

from urllib.request import urlopen
import json

html = urlopen("http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?situacaoFuncionamento=1&energiaInexistente=on&aguaInexistente=on&esgotoInexistente=on")
resposta = json.loads(html.read().decode('utf-8'))

print("Numero de escolas com energia, agua e esgoto tratado: ", resposta[0])

for e in resposta[1]:
    print(e["nome"], e["estado"], e["dependenciaAdministrativaTxt"])
    #print(e["estado"])


