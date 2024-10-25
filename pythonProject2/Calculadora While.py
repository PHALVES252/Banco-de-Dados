from time import sleep

num1=int(input("Primeiro valor"))
num2=int(input("Segundo valor"))

operador=0

while operador!=5:
   operador=int(input("[1]Adição\n"
         "[2]Mutiplicação\n"
         "[3]Maior numero\n"
         "[4]Novos numeros\n"
         "[5]Finalizando o programa"))

   if operador==1:
     print(f'{num1}+{num2}={num1+num2}')
   elif operador==2:
     print(f'{num1}*{num2}={num1*num2}')
   elif operador==3:
     print(f'entre {num1} e {num2} o maior é {max(num1,num2)}')
   elif operador==4:
     num1=int(input("Primeiro valor"))
     num2=int(input("Segundo valor"))
   elif operador==5:
     sleep(2)
     print("Finalizando o programa")
   else:

     print('Opção invalida')


print("Programa encerrado")