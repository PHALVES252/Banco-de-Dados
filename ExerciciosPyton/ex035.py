print("Calculadora de salario")

salario=float(input("Digite seu salario atual"))
ajuste1=salario*10/100
ajuste2=salario*15/100

if salario>1250:

    print("Quem ganhava {} passará a ganhar {} ".format(salario, salario+ajuste2))

else:

    print("Quem ganhava {} passará a ganhar {}".format(salario, salario+ajuste2))