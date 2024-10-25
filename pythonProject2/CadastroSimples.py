cadastro={'nome':[],'sexo':[],"ano":[]}



while True:
    terminar=input("Deseja cadastrar uma pessoas [S|N]")


    if terminar in "nN":
        break

    if terminar.upper() not in "S":
        print("Digite S para sim e N para não")
        continue

    nome=input("Digite seu nome")
    sexo = input("Qual seu sexo")
    ano = int(input("Ano de nascimento"))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)



print(cadastro)