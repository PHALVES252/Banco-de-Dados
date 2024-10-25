from random import  randint
from time import sleep
from operator import itemgetter
lista={'Jogador 1':randint(1,6),
       'Jogador 2':randint(1,6),
       'Jogador 3': randint(1,6),
       'Jogador 4': randint(1,6)


       }
ranking=dict()

for k,v in lista.items():
    print(f' jogador {k} jogou {v}')
    sleep(1)


ranking= sorted(lista.items(), key=itemgetter(1), reverse=True)
print(ranking)
