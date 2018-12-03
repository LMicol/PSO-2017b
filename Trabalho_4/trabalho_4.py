import os
import sys
import datetime


def pretty_notation(tamanho):
    suffixos = [' B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while tamanho >= 1024 and i < len(suffixos)-1:
        tamanho /= 1024.
        i += 1
    f = ('%.f' % tamanho).rstrip('0').rstrip('.') + suffixos[i]
    return f.rjust(6-len(f)+len(f)) 

        

def main_(path):
    arqs = []

    for file in os.listdir(path): 
        caminho = path + '/' + file 
        try:
            data_mod = str(datetime.datetime.fromtimestamp(os.path.getmtime(caminho))) 
            tamanho = os.path.getsize(caminho) 
            arqs.append(data_mod[:data_mod.find(' ')] + ' ' + pretty_notation(int(tamanho)) + ' ' + caminho)
            if os.path.isdir(caminho):
                arqs = arqs + main_(caminho) 
        except:
            arqs.append('Permissao de leitura negada para > ' + caminho)
    return arqs


        
def main():
    try:
        if not os.path.isdir(sys.argv[1]):
            return
        arq = main_(sys.argv[1])
        arq.sort()

        for path in arq:
            print(path)

    except:
        print('ERRO DURANTE A LEITURA DO CAMINHO')
  
main()

