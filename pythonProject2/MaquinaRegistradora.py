print("Maquina registradora")
print("-----=--"*10)

print("Vamos a compras")
precotot=0
cont=0


while True:
    codigo=float(input("Digite com o codigo do produto"))

    if codigo==0:
       break

    quant=int(input("Em quantas quantidade"))

    if codigo==1:
     preco=0.5


    cont=cont+quant
    precotot=preco*quant

print(f'{precotot}')



print('Progama finalizado')