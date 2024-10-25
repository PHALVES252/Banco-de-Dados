

# -----------FUNÇÃO PARA ENTRADA DO TIPO DE SERVIÇO------------------#
def escolha_servico():
    while True:
        try:
            servico = input("Escolha o serviço que deseja:\n"
                            "DIG para digitalização\n"
                            "ICO para impressão colorida\n"
                            "IBO para Foto preto e branco\n"
                            "FOT para Fotocopia : ")

            if servico.isalpha(): #UTILIZADO PARA ACEITAR A ENTRADA COM LETRA MAISCULA OU MINUSCULA
                servico = servico.upper()
                if servico == "DIG":
                    return 1.10
                elif servico == "ICO":
                    return 1
                elif servico == "IBO":
                    return 0.40
                elif servico == "FOT":
                    return 0.20
                else:
                    print("Serviço digitado incorretamente, escolha o codigo certo")

        except ValueError:
            print("Não são permitidos valores numéricos.")

# -----------FUNÇÃO PARA ENTRADA PARA ESCOLHA DO NUMERO DE PAGINAS------------------#
def num_pagina():
    contpag = 0
    while True:
        try:
            quant = int(input("Entre com a quantidade de cópias que deseja: "))
            contpag = quant

            if quant < 20:
                return 0, contpag

            elif quant >= 20 and quant < 200:
                return 0.15, contpag
            elif 200 <= quant and quant < 2000:
                return 0.2, contpag
            elif 2000 <= quant and quant < 20000:
                return 0.25, contpag
            else:
                print("Não são aceitas cópias nessa quantidade")

        except ValueError:
            print("Digite apenas valores numéricos")

# -----------FUNÇÃO PARA ENTRADA CASO CLIENTE QUEIRA SERVIÇO EXTRA------------------#
def servico_extra():
    acumuladora = []
    contador = 0

    while True:
        try:
            extra = int(input("Você deseja um serviço extra: 1 para Encadernação simples, 2 para Encadernação com capa dura ou 0 se não desejar mais nada: "))

            if extra == 1:
                acumuladora.append(10)
                contador += 1
            elif extra == 2:
                acumuladora.append(40)
                contador += 1
            elif extra == 0:
                return sum(acumuladora), contador
            else:
                print("Inválido, digite 1 ou 2")
        except ValueError:
            print("Apenas valores numéricos")




            # -----------PROGRAMA PRINCIPAL------------------#


print("Bem-vindo à Papelaria do Paulo")

escolhaservico = escolha_servico()
preco_por_pagina, numpagina = num_pagina()
adicional, quantidade = servico_extra()

total = (escolhaservico * preco_por_pagina * numpagina) + adicional

print("Total a pagar é: R${:.2f}".format(total))
print("quantidade de folhas:", numpagina)

print("A quantidade de adicionais é:", quantidade)
