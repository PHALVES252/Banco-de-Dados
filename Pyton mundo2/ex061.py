primeiro=int(input("Digite o termo"))
termo=primeiro
raza=int(input("Entre com a razaão"))
cont=1
total=0
mais=10
while mais!=0:
    total=total + mais
    while cont<=total:

        print(termo, end='->')

        termo=termo+raza
        cont=cont+1







    print('PAUSA', end='  ')
    mais=int(input('Quantos termos você quer que apareça a mais'))
print(f'{total} termos')
print("Fim")
