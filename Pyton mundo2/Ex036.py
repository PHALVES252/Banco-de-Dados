print("Calcule se você tem direito a um emprestimo\n")





casa=float(input("Entre com o valor da casa em R$:"))
sala=float(input(" Salario do comprador:"))
tempo=int(input("Quantos anos de financiamento" ))

mensalidade=casa/(tempo*12)
salarioReal=(30*sala)/100

print("30% de é igual a {} ".format(salarioReal))

print("Para pagar um casa de {:.0f} em {} anos o valor da prestação será de {:.2f}".format(casa,tempo, mensalidade))
if mensalidade>salarioReal:

    print("\033[0;40;31m Emprestimo negado ")

elif mensalidade<=salarioReal:

    print("Emprestimo concedido")





