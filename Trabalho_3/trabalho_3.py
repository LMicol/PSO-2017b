import collections
import requests
import json
import sys

def total_de_pacotes():
    arquivo = open(sys.argv[1], 'r')
    print("       Numero total de Pacotes: \n")
    print(len(arquivo. readlines()))


def top10_SRC():
    arquivo = open(sys.argv[1], 'r')
    source = []
    print("\n       Top 10 pacotes fontes: \n")
    for l in arquivo:
        aux = l[l.find("SRC=")+4:]
        source.append(aux[:aux.find(" ")])
        
    arquivo.close()

    source = collections.Counter(source)
    for (a,b) in source.most_common(10):
        pedido = requests.get("https://ipinfo.io/" + a)
        retorno = json.loads(pedido.text)
        try:
            print("Ocorrências: " + str(b)+ '  ' + "IP: " + a + "  "+ retorno ["country"] + "/"+retorno["city"])
        except:
            print("Ocorrências: " + str(b)+ '  ' + "IP: " + a)


            
def top10_DST():
    arquivo = open(sys.argv[1], 'r')
    source = []
    print("\n       Top 10 pacotes destino: \n")
    for l in arquivo:
        aux = l[l.find("DST=")+4:]
        source.append(aux[:aux.find(" ")])
        
    arquivo.close()

    source = collections.Counter(source)
    for (a,b) in source.most_common(10):
        pedido = requests.get("https://ipinfo.io/" + a)
        retorno = json.loads(pedido.text)
        try:
            print("Ocorrências: " + str(b)+ '  ' + "IP: " + a + "  "+ retorno ["country"] + "/"+retorno["city"])
        except:
            print("Ocorrências: " + str(b)+ '  ' + "IP: " + a)


            
def contagem_proto():
    print("\n       Contagem de Protocolos: \n")
    arquivo = open(sys.argv[1], 'r')
    protos = []
    for l in arquivo:
        aux = l[l.find("PROTO=")+6:]
        protos.append(aux[:aux.find(" ")])
        
    arquivo.close()

    protos = collections.Counter(protos)
    for (a,b) in protos.most_common(3):
        print("Ocorrências: " + str(b)+ '  ' + "Proto: " + a)


    
def top10_usage():
    print("\n       Top 10 portas: \n")
    arquivo = open(sys.argv[1], 'r')
    portas = []
    for l in arquivo:
        aux = l[l.find("DPT=")+4:]
        portas.append(aux[:aux.find(" ")])
            
    arquivo.close()

    portas = collections.Counter(portas)
    for (a,b) in portas.most_common(10):
        print("Ocorrências: " + str(b)+ '  ' + "Porta: " + a)




total_de_pacotes()
top10_SRC()
top10_DST()
contagem_proto()
top10_usage()
