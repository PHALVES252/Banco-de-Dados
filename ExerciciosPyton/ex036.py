print("Voce gostaria de saver como um triagulo é formado?\n")

print("Primeiro será nescessario que entre com o cumprimento de tres retas")

reta1=float(input("Difite o cumprimento da primeira reta"))
reta2=float(input("Digite o cumprimento da segunda reta"))
reta3=float(input("Digite o cumprimeento da terceira reta"))

if  reta3<reta2+reta1 and reta2<reta3+reta1 and reta1<reta3+reta2:

    print("Os segmentos podem formar um triangulo")

else:

    print("Os segmentos nao podem formar um triagulo")

