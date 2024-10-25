from datetime import date
atual=date.today().year


print("Confederação nacional de natação")

ano=int(input("Para saber sua classificação, por gentileza digite seu anos de nascimento"))
idade=atual-ano

print("Você tem {} anos".format(idade))


if idade<=9:

    print(" Sua classificação é \033[0;32mMIRIN")


elif idade<=14:

    print("Sua classificação é \033[0;34mINFANTIL")

elif idade<=19:
    print("Sua classificação é \033[0;36mJUNIOR")

elif\
        idade<=25:
    print("Sua classificação é \033[0;37M SENIOR")

else:
    print("Sua classificação é \033[0;31m MASTER")



