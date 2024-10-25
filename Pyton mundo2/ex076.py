

lista=("Lapis", 1.75 ,
       "Borracha", 2,
       "Caderno",15.90)




for item in range(0,len(lista)):

    if item%2==0:
        print(f"{lista[item]:.<30}",end=" ")

    else:
        print(f"R${lista[item]:>7.2f}")




