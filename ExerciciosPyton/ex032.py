print("Esse programa foi incrito para que você saiba quanto pagará pela viagem")

distancia=int(input("Entre com a distancia em quilometros"))


if distancia<=200:

    print("Sua viagem será de {} e o preço que irá pagar será de {:.0f}R$".format(distancia,distancia*0.50))



else:

    print("Sua viagem será de {} e o preço que irá pagar será de {}".format(distancia,distancia*0.45))


print("Fim do programa")