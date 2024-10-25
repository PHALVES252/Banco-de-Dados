

lista=[]
listapar=[]
listimpar=[]


while True:
    num=int(input("Digite um numero"))
    lista.append(num)
    resp=input("Deseja continuar")

    if resp in "nN":
        break

    elif num%2==0:
        listapar.append(num)

    else:
        listimpar.append(num)



print(f"Essa é a lista completa {lista}")
print(f"Essa é a lista de numeros pares {listapar}")
print(f" Essa é a lista de numeros impares {listimpar}")