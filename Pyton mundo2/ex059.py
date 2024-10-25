
num1=int(input("Primeiro valor"))
num2=int(input("Segundo valor"))

operador=0

while operador!=5:
    operador = int(input("Escolha uma operação\n"
                         "[1] Adição\n"
                         "[2]Mutiplicação\n"
                         "[3] Maior numero\n"
                         "[4] Novos numeros\n"
                         "[5] Sair do programa"))


    if operador==1:
        print(f'{num1}+{num2}={num1+num2}')

    elif operador==2:
        print(f'{num1}*{num2}={num1 * num2}')
    elif operador==3:
        print(f'O mairo numero é {max(num1,num2)}')
    elif operador==4:
        num1 = int(input("Primeiro valor"))
        num2 = int(input("Segundo valor"))



    elif operador==5:
       print("Finalizando")
    else:
        print("opção invalida")

print("Fim do programa volte sempre")