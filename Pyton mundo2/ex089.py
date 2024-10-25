

ficha=list()

while True:

    nome=input("Nome: ")
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    media=(nota1+nota2)/2

    ficha.append([nome,[nota1,nota2],media])

    resp=input("Deseja continuar [S|N]")


    if resp in "nN":
        break

print("==="*30)
print(f"{"NO.":<4} {"Nome":<10} {"Media":<8}")
print("===="*20)

for i,v in enumerate(ficha):
    print(f"{i:<4} {v[0]:} {v[2]:>8}")

while True:
    opc=int(input("Qual a nota voce deseja ver ou 999 para sair"))

    if opc==999:
        break


    if opc<=len(ficha)-1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")

print("Volte sempre")





