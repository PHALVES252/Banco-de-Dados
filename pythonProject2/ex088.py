from random import randint
lista=list()
jogos=list()
cont=0
tot=1

quant=int(input("Quantos jogos você deseja que eu sorteie"))
while tot<=quant:
    cont=0
    while True:
        num=randint(1,60)

        if num not in lista:

            lista.append(num)
            cont=cont+1

        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot=tot+1

print(f"Sorteando {quant} jogos")


for i, l in  enumerate(jogos):
    print(f"jogo {i+1} :{l} ")




