

from random import randint
from time import sleep

computador=randint(0,5)  # Faz o computador pensar
print("--||---"*20)
print("Pensei em numero, tente adivinhar")
print("--||---"*20)

numero=int(input("Em que numero pensei? "))

print("Processando.......")
sleep(2)
if numero==computador:

    print("Parabens voce venceu")

else:

    print("Não foi dessa vez")