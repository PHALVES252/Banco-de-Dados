

listanum=[]
maior=0
menor=0

for c in range(0,5):
    num=int(input(f"Digite um numero na posição {c} "))
    listanum.append(num)

    if c==0:
        maior=menor=listanum[c]

    else:
        if listanum[c]>maior:
            maior=listanum[c]

        if listanum[c]<menor:
            menor=listanum[c]

print(f"Você digitou os valores {listanum}")
print(f"Os maiores valores digitados foi {maior}nas posições",end=" ")



for i,v in enumerate(listanum):
    if v==maior:
        print(f"{i}.....",end=" ")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end=" ")

for i,v in enumerate(listanum):
    if v==menor:
        print(f"{i}......",end=" ")


