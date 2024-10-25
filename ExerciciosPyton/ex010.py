print("Conversor de moedas")

num=float(input("Entre com o valor em reais "))


print("{:.2f} R$ valem {:.2f} US$ (Estados Unidos)".format(num, (num/5.70)))
print("{} R$ valem a {:.2f} Euros (Paises que pertencem a União Europeia)" .format(num, (num/6.05)))
print("{} R$ valem a {:.2f} Libras (Reino unido)" .format(num,(num/7.21)))
print("{} R$ valem {:.2f} Ienes (Japão)".format(num,(num/0.0478)))

print("")

