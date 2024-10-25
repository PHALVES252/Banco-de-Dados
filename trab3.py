





# Função para escolha do tipo de madeira
def escolha_tipo():

    while True:

        try:
            mad=input("Entre com o tipo de madeira desejado\n"
                        "PIN----Tora de Pinho\n"
                        "PER----Tora de Peroba\n"
                        "MOG----Tora de Mogno\n"
                        "IPE----Tora de IPÊ\n"
                        "IMB----Tora de Inbuia ")

        # Verifique se o que foi digitado é alfabetico e converte para maiscula
            if mad.isalpha():
                mad=mad.upper()

            if mad=="PIN":
                return 150.40
            elif mad=="PER":
                return 170.20

            elif mad=="IPE":
                return 210.10
          #Caso o cliente  digite o que não está dentro do escopo de opções
            else:
                print("Serviço digitado incorretamente")
     #Para casos em que usuario digite valores numericos
        except ValueError:
            print("Não é permitido Valores numericos")



#Função para escolher a quantidade de toras
def qtd_toras():
    contT=0
    while True:

        try:

            quant=int(input("Por favor entre com a quantidade de toras"))
            contT=quant

            if quant<100:
                return 0,contT

            elif quant>=100 and quant<500:
                return 0.04,contT

            elif quant>=500 and quant<1000:
                return (9/100),contT

            elif quant>=100 and quant <=2000:
                return (16/100),contT

            else:
                print("Não são aceitos quantidades no valor informado")

        except ValueError:
            print("Digite apenas valores numericos")

# Função para escolha do tipo de transporte
def transporte():



        while True:

            try:
                trans=int(input("Entre com  o tipo de transporte\n"
                                "1--Tranporte Rodoviario---- R$ 1000\n"
                                "2--Transporte Ferroviario----R$ 2000\n"
                                "3--Transporte Hidrovriario----R$ 2500"))





                if trans==1:
                    return 1000

                elif trans==2:
                    return 2000

                elif trans==3:
                    return 2500

                else:
                    print("Opção incorreta, Apenas numeros de 1 a 3")

            except ValueError:
             print("Apenas valores numericos")





#PROGAMA PRINCIPAL


print("Bem vindo a madereira do Paulo Henrique")

escolhatipo=escolha_tipo()
desc,quant=qtd_toras()
via=transporte()


total=(escolhatipo*quant)*(1-desc)+via
print(f"{total:.2f}")
