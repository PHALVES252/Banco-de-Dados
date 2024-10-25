import math


print(" Calculadora para media ponderada ")

media=float(input("Digite a  media de aprovação "))

nota1=float(input("Digite a primeira nota "))
peso1=float(input("Digite o peso da nota 1 em % "))
nota2=float(input("Digite sua segunda nota "))
peso2=float(input("Digite o peso da nota 2 em % "))
nota3=float(input("Digite sua terceira nota "))
peso3=float(input("Digite p peso da nota 3 en % "))
nota4=float(input("Digite sua quarta nota "))
peso4=float(input("Digite o peso da nota 4 em % "))


result=(nota1*(peso1/100))+(nota2*(peso2/100))+(nota3*(peso3/100))+(nota4*(peso4/100))

mediaNescessaria=media-result
Arrend=math.ceil(result)
print("Sua media é {}".format(Arrend))


if result<70 and result==68:


 print("Aprovado")

elif result<68:
 Arrend = math.ceil(result)
 print(Arrend)
 print("Reprovado")
 print("Faltam {} pontos para que possa ser aprovado".format(mediaNescessaria))


