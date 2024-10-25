
from datetime import date


print("Progama destinada a calcular se um ano é Bissexto")

ano=int(input("Digite o ano com 4 digitos ou digite 0 para o ano atual"))

if ano==0:
    ano= date.today().year

calculo=ano%4
calculo2=ano%100
calculo3=ano%400


if calculo==0 and calculo3==0:

    print("O ano e bissexto")

else:

    print("{} não é um ano Bissexto".format(ano))