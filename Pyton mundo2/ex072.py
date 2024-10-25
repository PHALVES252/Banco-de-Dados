tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                   'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze', 'quatorze', 'quinze',
                   'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')



while True:
    numero=int(input("Digite um numero entre 0 e 20"))
    resp=input("Deseja continuar")


    if resp in "Nn":
        break




print(f'Você digitou o numero {tupla[numero]}')
