# num=[2,3,5,8,9,1,4]
#
#
#
# if 4 in num:
#     num.remove(4)
#     print("Numero eliminado")
# else:
#     print("Não existe numero 4 na sequencia")

valores=[]

for cont in range(1,5):
    valores.append(int(input("Digite um valores")))


for c,v in enumerate(valores):
    print(f"Encontrei {v} na posição {c}")


# listaA=[1,2,8,9]
# listaB=listaA[:]
# listaB[0]=2
# print(f"Lista A= {listaA}")
# print(f"Lista A= {listaB}")