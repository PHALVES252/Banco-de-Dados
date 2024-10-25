lista=[]



while True:
    num=int(input("Digite um numero"))

    if num not in lista:
        lista.append(num)
        print("Numero adicionado")

    else:
        print("Numero não adicionado")
    resp=input("Deseja continuar [N|S")


    if resp in "nN":
        break





print(sorted(lista))