# INICIO DO MENU CADASTRAR

lista_livros=[]
id_livro=0
def cadastrar_livro(id):
    print("------Menum de cadastro de livro")
    print("O oodigo do livro é {}".format(id))
    nome=input("Entre com o nome do livro \n")
    autor=input("Entre com o nome do autor do livro \n")
    editora=input("Entre com o nome da editora \n")


    #-------Criar dicionario

    dicionario_lista={ "id":id,
                       "nome":nome,
                       "autor":autor,
                       "editora":editora}

    print("Livro cadastrado com sucesso")

    lista_livros.append(dicionario_lista.copy())


    #FIM DO MENU CADASTRAR


    #INICIO DO MENU CONSULTAR

def consultar_livro():

        while True:
            op_consultar=input("------MENU DE CONSULTA DE LIVROS--------------\n"+
                               "------ESCOLHA A OPÇÃO DESEJADA--------------\n"+
                               "------1 - CONSULTAR TODOS OS LIVROS--------------\n"+
                               "------2 - CONSULTA LIVRO POR ID  --------------\n"+
                               "------3 - CONSULTAR LIVRO POR AUTOR------------\n"+
                               "------4 - Retornar------------\n")


            if op_consultar=="1":

                print("Voce selecionou a opção de consultar todos os livros")

                for livros in lista_livros:
                    for key,value in livros.items():
                        print("{}: {}".format(key,value))

            elif op_consultar=="2":

                print("Você escolhe a opção consultar livro por id")
                valor_id=int(input("Digite o id do livro"))
                for livros in lista_livros:
                    if livros['id']==valor_id:
                        print("Codigo disponivel")
                        print("----------------------------")
                        for key,value in livros.items():
                            print("{}:, {}".format(key,value))
                            print("--------------------------------")
                        else:

                            print("Não existe livro com o id informado, informe um id valido")


            elif op_consultar == "3":

                print("Você escolheu a opção de consultar livro por autor")

                valor_id = input("Entre com o nome do autor: ")

                autor_encontrado = False

                for livros in lista_livros:

                    if livros["autor"] == valor_id:

                        autor_encontrado = True

                        print("--------------------------")

                        for key, value in livros.items():
                            print("{}: {}".format(key, value))

                        print("--------------------------")

                if not autor_encontrado:
                    print("Autor inexistente, realize uma nova consulta com um autor válido")


            elif op_consultar == "4":

                return


            else:

                print("Opção inválida")
#-----------------------------FIM DO MENU CONSULTAR----------------------------------------------#

#-----------INICIO DO MENU REMOVER-------------------------------------------------------------------#
def remover_livro():
    print("------MENU REOVER LIVRO-------")
    valor_id = int(input("Entre com o numero do id do livro que deseja remover"))
    for livro in lista_livros:
        if livro['id'] == valor_id:
            lista_livros.remove(livro)
            print("Livro removido da lista de livros")
            print("-----------------------------------")

#------------------------FIM DO MEUN REMOVER-----------------------------------#



#----------------------------INICIO DE MAIN------------------------------------------#

print("Bem vindo a lista de controle de livros do Paulo Henrique")

while True:
    op= input("----------MENU PRINCIPAL \n"
              " Escolha a opção desejada\n"
              "1-Cadastrar livro\n"
              "2-Consultar livro\n"
              "3-Remover livro\n"
              "4-Sair\n")

    if op=="1":
        id_livro +=1
        cadastrar_livro((id_livro))
    elif op=="2":
        consultar_livro()

    elif op=="3":
        remover_livro()
    elif op=="4":
        break

    else:

        print("opção invalida")
        continue


#-----------------------FIM DO MAIN---------------------------------------#
