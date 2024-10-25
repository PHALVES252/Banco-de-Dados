num=int(input("Digite um numero"))
num2=int(input("Digite outro numero"))

s=num+num2
d=num/num2
sub=num-num2

pot=num**num2
inteiro=num//num2
rest=num%num2

raiz=num**(1/2)
raizc=num**(1/3)



print("A soma dos dois numeros é {}, o resultado da divisão é {:.3f} e a subtração é {}".format(s,d,sub))

print("O primeiro numero elevado ao segundo é {}, o resultado da divisão por inteiro é {} e o resto da divisão é {}" .format(pot,inteiro,rest))

print(" A raiz quadrada do primeiro numero {} é {:.2f} e a raiz cubica é {:.2f}".format(num,raiz, raizc))