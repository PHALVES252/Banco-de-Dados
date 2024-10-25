print("Calculadora salarial")

salar=float(input("Digite o quanto voce ganha por hora"))
hora=int(input("Digite  a quantidade de horas trabalhadas"))
liquido=salar*hora

print("De acordo com as informações fornecidas, um trabalho onde se ganha {}R$ por hora e com a quantidade horas trabalhadas que foi {}, Seu salario será de {}R$" .format(salar,hora,liquido))

if liquido<=1140:

    print("Você está abaixo da linha da pobreza")