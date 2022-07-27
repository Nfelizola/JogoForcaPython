###############################################################################
#             Nivaldo Felizola - unicesumar                                   #
###############################################################################
# Bom, aqui no início temos as bibliotecas que foram necessárias
from operator import length_hint
import time
import webbrowser
from pip import main
from MyDefs import *

# conjunto de imagens da forca com as fases do enforcado e a fase de vitorioso na posição 7
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
 
Chupa Python, eu Venci !!!!  
  O   
--|--
 / \  
======''']
palavra = sorteiopalavra()
x= length_hint(palavra)
vpista= extrairpista(palavra)
# construir painel da palavra sorteada
tracos=""
for i in range(x):
      tracos = tracos +("["+str(i+1)+"]")
      palavra= palavra.upper()
erros = 0
nletrasacertadas=0
ganhou=False
painelsuperior()
print("o Computador já retirou uma palavra da internet e ela tem "+str(x)+" letras")
print("você tem direito a 06 erros ")
nomejogador = input("por favor diga qual seu nome ou desista usando ctrl+c.. kkkkkk===>:")
# enquanto não estourar os erro não será enforcado
while erros<6 :
      painelsuperior()
      print(FORCAIMG[erros])
      print (tracos)
      if (nletrasacertadas>=int(x/2)):
            print("Pista destravada==>")
            print(vpista) 
      escolha = input("ok , "+nomejogador+",  Qual letra você quer arriscar?==>").upper() 
      acerto = palavra.count(escolha)
      if acerto >0 :
        print("oba temos estas letra sim...")
        time.sleep(2)
        pos = 0
        substituir=False
        while acerto != 0:
                pos = (palavra.find(escolha,pos))
                tracos = tracos.replace("["+str(pos+1)+"]",escolha,1)
                pos=pos+1
                nletrasacertadas= nletrasacertadas+ 1
                acerto = acerto -1
                
        if (tracos.find("[",0)==-1) :
            acerto=0
            ganhou=True
            erros=7
      else:
        print("errou")
        erros=erros+1
        print("você têm direito a mais "+ str(6-erros)+" erro(s)")
        time.sleep(2)
        
# chegando aqui ou foi enforcado ou a variável ganhou indicará como ganhador
if (ganhou==True):
            print (FORCAIMG[7])
            print ("oBAAA !!!! Temos um campeão você ganhou")
            print ("Parabéns "+ nomejogador +", você têm um ótimo vocabulário")
            print("a palavra "+ palavra + ", que significa: "+vpista)
            webbrowser.open("https://www.google.com/search?q="+palavra)
else:
            print (FORCAIMG[6])
            print("puxa vida "+ nomejogador +", você falhou miseravelmente, a palavra era: "+ palavra)
            print("")
            print("ou seja :"+vpista)
            print("")
            print("-------------- O QUE NÃO ESTÁ ACREDITANDO ?????????")
            resposta= input ("quer googar digite sim, ou qualquer outra coisa para finalizarmos:  ")
            if (resposta == "sim") :
                  webbrowser.open("https://www.google.com/search?q="+palavra)



