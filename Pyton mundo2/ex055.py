


# peso=int(input("Digite um peso"))
# pesp=int(input("Digite outro peso"))
#
# print(min(peso,pesp))

pesos=[]
for c in range(1,8):
    peso=float(input("Digite o peso da pessoa {} ".format(c)))
    pesos.append(peso)


print(f' A pessoa com o menor peso pesa{min(pesos)}')
print(f'A pessoa com maior peso pesa {max(pesos)}')





