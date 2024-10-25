print(("Conversão de bases"))

num=int(input("Digite um numero inteiro"))
print('''Escolha uma das opções para conversão:
[1] Binario
[2] Octal
[3] Hexadecimal
        ''')

opção=int(input("Escolha sua opção"))


if opção==1:

    print("{} Convertido para binario é igual a {}".format(num,bin(num)[2:]))

elif opção==2:

    print("{} Convertido para Octal é igual a {}".format(num,oct(num)[2:]))

elif opção==3:
    print("{} Convertido para Hexadecimal é igual a {}".format(num,hex(num)[2:]))

