#!/bin/bash

pacotes(){ 
  echo -e "\n	N�mero total de pacotes \n"
  sed -n '$=' $1
}

IPs_fonte(){
  echo -e "\n	Top 10 IPs fonte e quantos pacotes cada um\n"
  
  cat $1 |\
  egrep 'SRC=+.[^ ]*' -o |\
  sort | uniq -c |\
  sort -n -rn | head -10
}
 
IPs_destino(){
  echo -e "\n	Top 10 IPs destino e quantos pacotes cada um\n"
  
  cat $1 |\
  egrep 'DST=+.[^ ]*' -o |\
  sort | uniq -c |\
  sort -n -rn | head -10
}

protocolos(){
  echo -e "\n	Contagem Pacotes por Protocolos\n"
  
  cat $1 | egrep 'PROTO=+.[^ ]*' -o |\
  sort | uniq -c | sort -n -rn | head -3
}


top10portas(){
  echo -e "\n	Top 10 Portas\n"

  cat $1 |\
  egrep 'PROTO=UDP SPT=+.[^ ]*' -o |\
  sort | uniq -c | sort -n > .saida.txt

  cat $1 |\
  egrep 'PROTO=UDP .*' -o | cut -d' ' -f1,3 |\
  sort | uniq -c | sort -n > .saida2.txt

  paste -d'\n' .saida.txt .saida2.txt > .final.txt


  cat $1 |\
  egrep 'PROTO=TCP SPT=+.[^ ]*' -o |\
  sort | uniq -c | sort -n > .saida.txt

  cat $1 |\
  egrep 'PROTO=TCP .*' -o | cut -d' ' -f1,3 |\
  sort | uniq -c | sort -n > .saida2.txt

  paste -d'\n' .saida.txt .saida2.txt > .final2.txt

  paste -d'\n' .final.txt .final2.txt > .result.txt
  cat  .result.txt | sort -n -rn | head -10
}

