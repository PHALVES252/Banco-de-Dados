num=int(input("Digite um numero"))

un=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10


print("{} unidades".format(un))
print("{} dezenas".format(d))
print("{} centenas".format(c))
print("{} milhares".format(m))
