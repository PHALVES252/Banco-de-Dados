from random import randint

numero=randint(1,10),randint(1,10), randint(1,10),randint(1,10),randint(1,10)
print(f"Os numeros sorteados foram {numero}", end="")


for n in numero:
     print(f"{n}",end="")

print(f"\nO maior numero sorteado foi {max(numero)}")
print(f"O menor numeros sorteado foi {min(numero)}")