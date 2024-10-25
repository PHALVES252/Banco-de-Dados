nome=input("Qual o seu nome")

if nome=="Gustavo":
    print("Olá {} seu nome é bem bonito".format(nome))

elif nome=="Maria" or nome=="Pedro":
    print("Olá {} seu nome é bem comun no brasil".format(nome))

elif nome in(" Ana Barbara Claudio"):
    print("Olá {}  que nome feminino bonito".format(nome))
print("Tenha um bom dia")