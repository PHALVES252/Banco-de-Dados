
cont=0
soma=0
sempar=False
for c in range(1,7):
    numeros=int(input("Digite o valor {} ".format(c)))
    if numeros%2==0:
        soma=soma+numeros
        cont=cont+1
        sempar=True
if sempar:
    print(f"Dos numeros digitados {cont} são pares")
    print(f'A soma dos numero pares é igual a {soma}')

else:
    print("Voce não digitou nenhum numero par")
    #soma recebe soma=0 + numeros 4
    #soma recebe soma=4 + numero 2
    #soma recebe soma=6 +numero 7
    #soma recebe soma=13 + numero 4
    #soma recebe soma=17 +numero 3
    #soma rece soma =20 +numeo 1

    #print soma==21