# este arquivo concentra as rotinas usadas para organizar melhor o codigo
import requests
import requests
import json
import os

def sorteiopalavra():
    # usando a biblioteca de request e json conseguimos dar um GET na api pública
    # do https://api.dicionario-aberto.net/index.html e ele têm uma URI que escolhe uma
    # palavra já de maneira randômica
    request = requests.get("https://api.dicionario-aberto.net/random")
    dados = (json.loads(request.content))
    return dados['word']
def extrairpista(p):
    request = requests.get("https://api.dicionario-aberto.net/word/"+p)
    dados = (json.loads(request.content))
    xml=dados[0]['xml']
    inicio=xml.find("<def>")+5
    fim = xml.find("</def>")
    vpista = xml[inicio:fim]
    return vpista
def painelsuperior():
    os.system("cls")
    print("#########################################################################################################")
    print("#####  BEM VINDO AO JOGO X-TREME FORCA ##################################################################")
    print("#########################################################################################################")
    print("#########################################################################################################")
    print("#########################################################################################################")
    print("#########################################################################################################")
    print("#########################################################################################################")
    print("")
    print("")
