print('               Bem vindo a sorveteria do Paulo ')
print(' ------------------- ----Cardapio-------------------------------- ')
print('| N° de bolas| Sabor tradicional(tr)| Sabor premiun(pr)| Sabor especial(es)|')
print('|    1       |     R$6,00           |     R$7,00       |    R$8,00         |')
print('|    2       |     R$11,00          |    R$13,00       |   R$15,00         |')
print('|    3       |     R$15,00          |    R$18,00       |   R$21,00         |')
print('----------------------------------------------------------------------------')

acumulador = 0
while True:
    bolas = int(input('Digite o numero de bolas '))
    if bolas <= 0 or bolas > 3:
        print('Numero de bola de sorvete invalido entre com numero de 1 a 3 ')
        continue

    sabor = input('Entre com o valor desejado (tr/pr/es ')
    if sabor.lower() not in ['tr', 'pr', 'es']:  # Fará a verificação independente se a letra for maiscula ou minuscula
        print('Sabor invalido')
        continue
        # Sabor tradicional
    elif sabor == 'tr' and bolas == 1:
        print('Voce escolher o sabor tradicional e {} bola de sorvete'.format(bolas))
        acumulador = acumulador + 6
    if sabor == 'tr' and bolas == 2:
        print('Voce escolher o sabor tradicional e {} bola de sorvete'.format(bolas))
        acumulador = acumulador + 11
    elif sabor == 'tr' and bolas == 3:
        print('Voce escolher o sabor tradicional e {} bola de sorvete'.format(bolas))
        acumulador = acumulador + 15

        # Sabor premium
    elif sabor == 'pr' and bolas == 1:
        print('Voce escolher o sabor premium e {} bola de sorvete'.format(bolas))
        acumulador = acumulador + 7
    elif sabor == 'pr' and bolas == 2:
        print('Voce escolher o sabor premium e {} bola de sorvete'.format(bolas))
        acumulador = acumulador + 13
    elif sabor == 'pr' and bolas == 3:
        print('Voce escolher o sabor premium e {} bola de sorvete'.format(bolas))
        acumulador = acumulador + 18

        # Sabor Especial
    if sabor == 'es' and bolas == 1:
        print('Voce escolher o sabor especial {} bolas de sorvete'.format(bolas))
        acumulador = acumulador + 8
    elif sabor == 'es' and bolas == 2:
        print('Voce escolher o sabor especial {} bolas de sorvete'.format(bolas))
        acumulador = acumulador + 15
    else:
        print('Voce escolher o sabor especial {} bolas de sorvete'.format(bolas))
        acumulador = acumulador + 21

    # Enquanto o usuario digitar S, retorna para a primeira solicitação
    plus = input('Deseja pedir mais alguma coisa? S para sim e N para não')
    if plus.upper() != 'N':
        continue
    print('Preço Total é {}R$'.format(acumulador))
    print('Muito obrigado, volte sempre')

    break