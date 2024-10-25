

from random import randint

print("Estou pensando em um numero tente adivinhar")

acertou=False
palpite=0
computador=randint(1,10)
while not acertou:
    jogador=int(input("Sua vez"))
    palpite=palpite+1

    if computador==jogador:
        acertou=True
        print("Voce acertou, parabens")
        print(f"Voce acertou na {palpite} tentativa")

    else:

        if computador>jogador:
            print("Mais, tente mais uma vez")

        else:
            print("Menos, tente mais uma vez")

