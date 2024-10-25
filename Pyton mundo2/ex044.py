print("----------LOJA DO PAULO-------------")

valor=float(input("Digite o valor do produto "))

escolha=int(input("Formas de pagamento\n"
                  "[1] Pagamento a vista\n"
                  "[2] Á vista no cartão\n"
                  "[3]2x no cartão\n"
                  "[4]3x ou mais no cartão"))


if escolha==1:
    desc=valor*10/100
    print(f"Sua compra de R${valor} vai custar R${valor-desc} no final")

elif escolha==2:
    desc=valor*5/100
    print(f'Sua compra no valor de R${valor} vai custar R${valor-desc} no final')

elif escolha==3:
    parcela=valor/2
    print(f'Sua compra no valor de R${valor} ficará em 2 parcelas de R${parcela} cada')

elif escolha==4:
    quantParcela=float(input("Digite em quantas vezes deseja parcelar a compra"))

    if quantParcela>3:

        juros=valor*20/100
        ValorAjustado=valor+juros
        Valorparcelas = ValorAjustado / quantParcela

        print(f"Sua compra no valor de R${valor} parcelada em {quantParcela} vezes custará no final R${ValorAjustado}")
        print(f"O valor de cada parcela ficará R${Valorparcelas}")

    else:

        print("Numero de parcela não disponivel para essa opção, escolha 3 ou mais")

else:

    print("Opção invalida, escolha um numero de 1 a 4")