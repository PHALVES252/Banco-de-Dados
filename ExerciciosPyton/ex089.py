nomes=[]
galera=[]
maior=menor=0
while True:
    nomes.append(input("Digite seu nome"))
    nomes.append(float(input("Digite seu peso")))

    if len(galera)==0:
        maior=menor=nomes[1]


    else:
        if nomes[1]>maior:
            maior=nomes[1]

        if nomes[1]<menor:
            menor=nomes[1]





    galera.append(nomes[:])
    nomes.clear()
    resp=input("Deseja continuar [S|N]")


    if resp in "nN":
        break
print(f"A quantidade de pessoas cadastradas é igual {len(galera)}")
print(f'O maior peso é {maior} de',end=" ")


for p in galera:
    if p[1]==maior:
        print(f"{p[0]}",end=" ")
print(f"O menor peso é {menor}",end=" ")
for p in galera:
    if p[1]==menor:
        print(f"{p[0]}",end=" ")






