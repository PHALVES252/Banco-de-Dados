

print("Calculadora de regra de tres")

numero=int(input(" Digite um numero, pode ser em quantidade de quilos, kilometros "))
equivalente=(float(input("Digite agora o equivalente a que foi digitado anteriormente ")))

numero2=int(input("Digite agora o novo numero referente ao numero1 "))

calculo=(numero2*equivalente)/numero

print(f'com  {numero} eu teria {equivalente}')
print(f'agora se fosse{numero2} o resultado seria {calculo}')