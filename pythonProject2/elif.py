

nome= input("Digite seu nome")



if (nome=="Vinicius"):
    print("Ola {} seja bem vindo".format(nome))

elif(nome!="Vinicius"):
    idade=int(input("Digite sua idade"))

    if(idade<18):
       print("Voce é de menor")

    elif(idade>100):
          print("Alguem com essa idade provavelmente não existe")