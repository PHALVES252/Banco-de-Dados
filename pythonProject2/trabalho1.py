print("Bem vindo a loja do Paulo")

valorunit=float(input("Para começar digite o valor do produto que deseja comprar "))
quant=int(input("Agora digite a quantidade"))

#calculo total do produto
totalc=(valorunit*quant)

 #condições
if(totalc<250):
    desc=0
elif(totalc>=250 and totalc<600):
    valordesc=totalc*0.4
    print("O desconto aplicado para sua compra é de 4%")

elif(totalc>=600 and totalc<1000):
    valordesc=totalc*0.7
    print("O desconto aplicado para sua comproa é de 7%")


else:
    valordesc=totalc*0.11
    print("O desconto aplicado para sua comproa é de 11%")


 #Saida do console
print("O valor com desconto é {} R$" .format(totalc-valordesc))
print(("O valor sem desconto é {} R$".format(totalc)))