print("Calculadora de valores com Soma, Subtração, Divisão,Mutiplicação")


n1=int(input("Digite um numero "))
n2=int(input("Digite outro numero"))

s=n2+n1
m=n2*n1
d=n1/n2
su=n1-n2


di=n1//n2
e=n1**n2

print(" a soma é {}, a mutiplicação é {}, a divisão é {}, e a subtração é {}".format(s,m,d,su))

print("Para resto da divião, divisão por inteiro e ´potencia, vamos aproveitar os mesmos numeros digitados")

print(" O resto da divisão é {}, e a potencia é {}".format(di,e))

print("Para casas decimais no caso da divisão basta adicional o numero de cadas entre cochetes .3f, 3 casas decimais {:.3f}".format(d))