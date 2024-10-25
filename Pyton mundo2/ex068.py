from random import randint






cont=0
perdeu=True
soma=0

print("======"*12)
print("VAMOS JOGAR UM JOGO DE PAR OU IMPAR")

while perdeu==True:
    computador = randint(1, 10)
    print("======" * 12)
    jogador=int(input("Digite um numero "))
    cont=cont+1

    escolha=input("PAR OU IMPAR ")

    soma=jogador+computador

    print(f" Computador escolheu {computador} e voce {jogador} o total é {soma}",end=" ")
    print(f"Deu par" if soma%2==0 else "Deu impar")
    if escolha not in "pi":
        print("Voce digitou algo incorreto, verifique")

    elif (escolha=="p" and soma%2==0) or (escolha=="i" and soma%2!=0):
        print(" Você venceu")
        print("Vamos mais uma vez")

    else:
        print("Voce perdeu")
        perdeu=False

print(f"GAME OVER-- Você venceu {cont-1} vezes")
