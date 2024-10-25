print("-----------Bem vindo a  Pizzaria Do Paulo-------------")
print("-------------------Cardapio----------------------")

print("Tamanho |  Pizza Salgada (PS)   | Pizza Doce (PD")
print("  P     |     R$ 30,00          | R$ 34,00")
print("  M     |     R$ 45,00          | R$ 48,00")
print("  G     |     R$ 60,00          | R$ 66,00")

acumulador=0

#   # O while irá criar um loop infinito,
#   levando em consideração que o programa não tem um limite
# estabelecido de vezes para ser repetido, encerrando somente quando o cliente desejar
while True:

    Sabor=input("Entre com o sabor desejado da Pizza [PS para salgada ou PD Para doce: ")

    # Se o sabor que o cliente digita não for nenhum dos apresentados
    #     no menu, aparece a informação de invalido e pergunta novamente

    if Sabor not in "psPsPDpd":
        print("Sabor invalido")

        continue  #Continue faz com que o programa retorne a informação inicial
    tamanho=input("Entre com o tamanho Desejado da Pizza[P|M|G] :")

    if tamanho not in  "pPMmgG":
        print("Tamanho invalido")
        continue

   #Opção caso o cliente opte pela pizza Salgada


    if Sabor in "PSps":
        print(" Voce escolheu a pizza salgada", end="")

        #Sabor salgado Pizza Pequena
        if tamanho in "pP":
            valor=30
            print(" no tamanho p :", end="")
            print(f" R$ {valor:.2f}")
            acumulador=acumulador+valor


        # Sabor salgado Pizza Media
        elif tamanho in "Mm":
            valor = 45
            print(" no tamanho M :", end="")
            print(f" R$ {valor:.2f}")
            acumulador = acumulador + valor
            # O acumulador, acumula os valores referente ao pedido do cliente

        # Sabor salgado Pizza Grande
        elif tamanho in "gG":
            valor = 60
            print(" no tamanho G :", end="")
            print(f" R$ {valor:.2f}")
            acumulador = acumulador + valor

    # Opção caso o cliente opte pela pizza Doce

    if Sabor in "PDpd":
        print(" Voce escolheu a pizza Docê",end="")
        # Sabor Doce Pizza Pequena
        if tamanho in "pP":
            valor = 34
            print(" no tamanho p :", end="")
            print(f" R$ {valor:.2f}")
            acumulador = acumulador + valor


        # Sabor Doce Pizza Media
        elif tamanho in "Mm":
            valor = 48
            print(" no tamanho M :", end="")
            print(f" R$ {valor:.2f}")
            acumulador = acumulador + valor

        # Sabor Docê Pizza Grande
        elif tamanho in "gG":
            valor = 66
            print(" no tamanho G :", end="")
            print(f" R$ {valor:.2f}")
            acumulador = acumulador + valor


            #Toda vez que o clinte escolher um sabor de pizza e o tamanho
            # O programa irá pergunta se ele deseja continuar

    resp=input("Deseja continuar")


    #Caso ele deseje continuar, o continue faz com todas as perguntas sejam feitas novamente
    if resp in "sS":

        continue
    #Caso seje Não o break encerra o programa
    elif resp in "nN":
        break







#Valor total do pedido
print(f"O valor total a ser pago é R$ {acumulador:.2f}")