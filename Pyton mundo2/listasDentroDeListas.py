item=[]
mercado=[]
produto=0

while True:
    item.append(input("Digite o produto"))
    produto=produto+1

    item.append(int(input("Digite a quantidade")))
    mercado.append(item[:])
    item.clear()
    resp=input("Deseja continuar")

    if resp=="n":
        break



print(f" Foram comprados {produto} produtos")
print(mercado)

