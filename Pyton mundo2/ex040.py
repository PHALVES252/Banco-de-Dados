print("Calculadora de media")

nota1=float(input("Digite sua primeira nota"))
nota2=float(input("Digite sua segunda nota"))

media=(nota1+nota2)/2

print("Sua media foi {}".format(media))
if media<5:

    print("\033[0;33m REPROVADO")

elif media>=5 <=6.9:

    print("\033[0;31m RECUPERAÇÃO")

else:

    print("Aprovado")