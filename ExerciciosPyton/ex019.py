from random import choice

nome1=input("Digite o primeiro nome")
nome2=input("Digite o segundo nome")
nome3=input("Digite o terceiro nome")
nome4=input("Digite o quarto nome")

lista=[nome1,nome2,nome3,nome4]
lista2=[nome1,nome2,nome3,nome4]
escolhido=choice(lista)
escolhido2=choice(lista2)

print("O primeiro selecionado será {}".format(escolhido))
print("O segundo selecionado será {}".format(escolhido2))