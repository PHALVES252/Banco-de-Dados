nome=str(input("Por favor digite seu nome")).strip()
nome.upper()
 # metodo strip compila tudo em uma só cadeira de carcteres
print(nome.strip(nome))
print("O nome tem silva no nome ?: {}".format("silva"in nome))