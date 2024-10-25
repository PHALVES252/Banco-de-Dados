

print("Calculadora Matematica")
print("Escolha a operação que deseja realizar \n"
           "+ Para adição \n"
           "- Para subtração \n"
           "/ Para Divisão \n"
           "* Para Mutiplicação")

ope=input(" Esoolha a operação que deseja realizar")

if ope == "+" or ope == "-" or ope == "/" or ope == "*":
    num1 = int(input("Digite o primeiro numero"))
    num2 = int(input("entre com o segundo numero"))

while ope!="s":



    if ope=="+":
        result=num1+num2
        print("Resultado de {} e {} é {}".format(num1, num2,result))


    elif ope=="-":
        result=num1-num2
        print("Resultado de {} e {} é {}".format(num1, num2,result))
    elif ope=="/":
        result=num1/num2
        print("Resultado de {} e {} é {}".format(num1, num2,result))

    elif ope=="*":
        result=num1*num2
        print("Resultado de {} e {} é {}".format(num1, num2,result))

    else:
        print("Operação invalida")

    ope = input(" Esoolha a operação que deseja realizar")

    if ope == "+" or ope == "-" or ope == "/" or ope == "*":
        num1 = int(input("Digite o primeiro numero"))
        num2 = int(input("entre com o segundo numero"))


    print("Encerrando o programa")



