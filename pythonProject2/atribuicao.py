valorprod=int(input(" Digite o valor do produto"))
valordesc=int(input(" Digite o desconto"))

desc=(valordesc/100)*valorprod

print("o desconto de  {}% lhe dará uma economia de {} R$, sendo assim o preço que irá pagar será de {} R$".format(valordesc,desc,valorprod-desc))
