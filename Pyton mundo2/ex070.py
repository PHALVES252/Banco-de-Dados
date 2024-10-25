
total=0
totmil=0
menor=0
barato=''
cont=0

while True:
    produto=input("Digite o nome do produto")
    preco=float(input("Digite o preço do produto"))

    resp=input("Deseja continuar [S/N]")
    total+=preco
    cont+=1

    if preco>1000:
        totmil=totmil+1

    if cont==1:
        menor=preco
        barato=produto

    else:

        if preco<menor:
            menor=preco
            barato=produto







    if resp in "nN":
        break






print(f" Valor total da compra {total} R$")
print(f" Há {totmil} produtos que custa mais de 1000 reais")
print(f'O produto mais barato custa {menor} e é {barato}')