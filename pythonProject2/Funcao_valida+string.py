def valida_string(pergunta, min, max):
    s1=input(pergunta)
    tam=len(s1)
    while ((tam<min) or (tam>max)):
        s1=input(pergunta)
        tam=len(s1)
    return s1


x=valida_string("Digite uma estring",10,30)
print("Voce digitou a estring {} encerrando programa".format(x))