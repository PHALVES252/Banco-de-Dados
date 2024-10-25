lista_contatos = []
id_contato = 0

# INICIO DO CADASTRAR CONTATO
def cadastrar_contato(id):
    print("Menu de cadastro de Contatos")
    print(f"O código de cadastro é {id}")
    nome = input("Digite o nome do contato: ")
    atividade = input("Qual sua atividade: ")
    telefone = input("Digite seu telefone: ")

    # Criar dicionário
    dicionario_lista = {"id": id,
                        "nome": nome,
                        "atividade": atividade,
                        "telefone": telefone}

    print("Contato cadastrado com sucesso")

    lista_contatos.append(dicionario_lista.copy())

# Fim do cadastrar contato

# INICIO DO CONSULTAR CONTATO
def consultar_contatos():
    while True:
        op_consultar = input("-MENU DE CONSULTA DE CONTATOS\n"
                             "-ESCOLHA UMA OPÇÃO QUE DESEJA\n "
                             "1----CONSULTAR TODOS\n "
                             "2----CONSULTAR POR ID\n "
                             "3----CONSULTAR POR ATIVIDADE\n "
                             "4----SAIR\n")

        if op_consultar == "1":
            print("Você selecionou a opção de consultar todos os contatos")
            for contatos in lista_contatos:
                for key, value in contatos.items():
                    print(f"{key}: {value}")
                print("-------------------")

        elif op_consultar == "2":
            print("Você selecionou a opção de consultar contato por ID")
            valor_id = int(input("Digite o ID do contato: "))

            contato_encontrado = False

            for contatos in lista_contatos:
                if contatos["id"] == valor_id:
                    contato_encontrado = True
                    print("==================")
                    for key, value in contatos.items():
                        print(f"{key}: {value}")
                    print("==================")
                    break  # Sai do loop após encontrar o contato

            if not contato_encontrado:
                print("Não existe um contato com o ID informado.")

        elif op_consultar == "3":
            print("Você selecionou a opção de consultar contatos por atividade")
            valor_atividade = input("Digite a atividade do contato: ")

            contato_encontrado = False

            for contatos in lista_contatos:
                if contatos["atividade"] == valor_atividade:
                    contato_encontrado = True
                    print("=============================")
                    for key, value in contatos.items():
                        print(f"{key}: {value}")
                    print("=============================")

            if not contato_encontrado:
                print("Não existe contato com a atividade informada.")

        elif op_consultar == "4":
            return

# INICIO DO REMOVER CONTATO
def remover_contato():
    print("Você selecionou a opção remover contato")
    valor_id = int(input("Entre com o ID do contato que deseja remover: "))

    contato_removido = False

    for contatos in lista_contatos:
        if contatos['id'] == valor_id:
            lista_contatos.remove(contatos)
            contato_removido = True
            print("Contato removido da lista")
            break

    if not contato_removido:
        print("Contato não encontrado.")

# PROGRAMA PRINCIPAL
print("Bem vindo à lista de contatos do Paulo Henrique")

while True:
    op = input("1---- Cadastrar contato \n"
               "2---- Consultar contato\n"
               "3---- Remover contato\n"
               "4---- Sair\n")

    if op == "1":
        id_contato += 1
        cadastrar_contato(id_contato)

    elif op == "2":
        consultar_contatos()

    elif op == "3":
        remover_contato()

    elif op == "4":
        print("Encerrando o programa.")
        break
