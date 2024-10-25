from random import choice
from random import randint
from time import sleep

itens=('Pedra','Papel','Tesoura')
computador= randint(0,2)




jogador=int(input("Escolha: \n"
                   "[0] Pedra\n"
                   "[1] Papel\n"
                   "[2]Tesoura\n"))

print("=="*10)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador escolheu {itens[jogador]}")
print("=="*10)


print("JO")
sleep(1)
print("QUEM")
sleep(1)
print("PO")
sleep(1)

print("Analisando jogadas")
sleep(1)
print("....")
sleep(1)
print(".......")
sleep(5)
if computador==0:

    if jogador==0:
        print("EMPATE")
    elif jogador==1:
        print("JOGADOR Vence")
    elif jogador==2:

        print("COMPUTADOR VENCE")
    else:

        print("Jogada Invalida")

elif computador==1:# COMPUTADOR ESCOLHEU PAPEL
   if jogador == 0: #PEDRA
        print("COMPUTADOR GANHA")
   elif jogador == 1: #PAPEL
       print("EMPATE")
   elif jogador == 2: #TESOURA
      print("JOGADOR GANHA")

   else:

        print("Jogada Invalida")

elif computador==2: #TESOURA

   if jogador == 0: #PEDRA
        print("JOGADOR GANHA")
   elif jogador == 1:#PAPEL
        print(" COMPUTADOR GANHA")
   elif jogador == 2: #TESOURA
        print("EMPATE")
   else:

        print("Jogada Invalida")












