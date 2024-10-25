
lista=[]


while True:
    num=int(input("Digite um numero"))
    lista.append(num)
    lista.sort(reverse=True)

    resp=input("Quer continuar? [S|N]")

    if resp in "Nn":
        break




print(f"Foram digitados {len(lista)} numeros")
print(f" A lista do menor para o maior é {lista}")

if 5 in lista:
        print("O numero 5 faz parte da lista ")

else:
    print("O numero 5 não faz parte da lista")