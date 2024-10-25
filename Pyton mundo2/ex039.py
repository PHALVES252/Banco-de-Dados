from datetime import date
atual=date.today().year


ano=int(input("Digite seu ano de nascimento"))
idade=atual-ano

print("Voce tem {} anos de idade".format(idade))

if idade==18:
    print("Você  está na idade de alistar")

elif idade>18:
    print("Você já passou do tempo de se alistar")
    print("Voce deveria ter se alisstado há {} anos atras".format(idade-18))
    print("Seu alistamento foi em {}".format(atual-(idade-18)))

else:

    print("Voce ainda não está na idade do alistamento, falta ainda {} anos para se alistar".format(18-idade))
    print(" A data aproximada para seu alistamento será em {}".format(ano+18))
