print("Calculadora de descontos")

valor=float(input("Entre com o preço do produto \n"))
vdesc=valor*5/100
valorf=valor-vdesc

print("O Produto que custa {:.0f}R$ como terá uma desconto de 5% passará a pagar {}R$".format(valor, valorf))