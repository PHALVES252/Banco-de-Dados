print("Voce gostaria de saber como um triagulo é formado")

print("Primeiramente sera´nescessario  que entre com o cumprimento das tres retas")


reta1=float(input("Digite o cumrprimento da primeira reta "))
reta2=float(input("Digite o cumrprimento da segunda reta reta "))
reta3=float(input("Digite o cumrprimento da terceira reta "))



if  reta3<reta2+reta1 and reta2<reta3+reta1 and reta1<reta3+reta2:

    if reta1==reta2==reta3:
        print("O triagulo é equilatero")

    elif reta1!=reta2!= reta3!=reta1:
        print("O triaguloo é escaleno")

    else:
        print("O triagulo é isoceles")

else:

    print("Os lados não podem formar um triagulos")