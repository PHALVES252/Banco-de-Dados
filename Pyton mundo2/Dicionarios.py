#  # LISTAS DENTRO DE UM DICIONARIO
#
#
# lanche={"Pão":["Centeio","Gergelim","Cenoura e Mel"],"Recheio":["Mortadela","Presunto","Peito de Peru"],"Bebida":['Achocolatador','Suco','Suco de soja']}
# print(lanche)
#
# for keys, values in lanche.items():
#     print(f'{keys}={values}')


   # LISTAS DENTRO DE DICIONARIO  RECEBENDO VALORES DO USUARIO


# lanche={"Pão":[],"Recheio":[],"Bebida":[]}
#
# for i in range(1,3):
#     Pão=input("Digite o tipo de pão que deseja\n"
#               "Centeio\n"
#               "Gergelim\n"
#               "Aveia\n")
#     Recheio=input("Entre com o recheio")
#     Bebida=input("Qual a bebida?")
#
#     lanche["Pão"].append(Pão)
#     lanche["Recheio"].append(Recheio)
#     lanche["Bebida"].append(Bebida)
#
# print(lanche)


    # DICIONARIOS DENTRO DE LISTAS

# lanche=[]
#
#
# lanche1={"PÃO":"CENTEIO","RECHEIO":"MORTADELA","BEBIDA":"ACHOCOLATADO"}
#
# lanche2={"PÃO":"GERGELIM","RECHEIO":"PRESUNTO","BEBIDA":"SUCO"}
#
# lanche3={"PÃO":"CENOURA E MEL","RECHEIO":"PEITO DE PERU","BEBIDA":"SUCO DE SOJA"}
#
# lanche=[lanche1,lanche2,lanche3]
#
#
#
#
# for c in lanche:
#     print(c)


  # DICIONARIOS DENTRO DE LISTAS RECEBENDO VALORES DO USUARIOS

  # gamesLista=[]
# gamesDicionario={}
#
#
# for i in range(1,4):
#     gamesDicionario['Nome']=input("Digite o nome do jogo")
#     gamesDicionario['Plataforma']=input("Qual a plataforma?")
#     gamesLista.append(gamesDicionario.copy())
#
#
# print(gamesDicionario)
    # print(gamesLista)


nome=input("Digite seu nome")[0]

while nome==nome[0].lower():
    print(" O nome tem que iniciar com letra maiscula")


