print("Aluguel de Carros ")

dias=int(input("Digite a quantidade de dias em que alugou o carro "))
km=int(input("Digite a quantidade de Kilometros rodados"))

valortotal=(km*0.15)+ (dias*60)

print(" Voce alugou o carro por {} dias e percorreu durante esse tempo {} kilometros, o preço a pagar será de {} R$".format(dias,km,valortotal))