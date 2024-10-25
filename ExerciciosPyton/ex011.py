print("Pintando uma parede")

alt=float(input("Entre com a altura da parede"))
larg=float(input("Entre com a largura da parede"))
area=alt*larg

print(" A parede tem uma dimensão de {} x {} e sua area é de {} m2".format(alt, larg,area))

print(" Para pintar uma parede de dois metros você irá precisar de {}L de tinta".format(area/2))