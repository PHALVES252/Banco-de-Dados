print("Calculadora de indice de massa corporal")

peso=float(input('Primeiro entre com seu peso em KG'))
altura=float(input("Agora entre com seu Altura "))

imc=peso/(altura*altura)

print(f"Seu imc é {imc:.2f}")

if imc<18.5:

    print("Você está abaixo do peso")

elif imc>=18 and imc <=25:

    print("Parabens Peso Ideal")

elif imc>25 and imc <=30:
    print("Sobrepeso")

elif imc>30 and imc<=40:
    print("Obesidade")

else:
    print("Obesidade Morbida")
