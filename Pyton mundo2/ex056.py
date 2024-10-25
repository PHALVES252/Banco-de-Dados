
somaidade=0
mediaidade=0
maioridadehomen=0
nomevelho=''
mulhertot20=0


for c in range(1,4):
    nome=(input(f"Digite o nome da {c} pessoa ")).strip()

    idade=int(input('Digite sua idade'))

    sexo=(input("Qual o sexo, [F/M]")).upper().strip()
    somaidade=somaidade+idade

    if c==1 and sexo in "mM":
        maioridadehomen=idade
        nomevelho=nome

    if sexo in "Mm" and idade>maioridadehomen:
        maioridadehomen=idade
        nomevelho=nome

    if sexo in"Ff" and idade>20:
        mulhertot20=mulhertot20+1


mediaidade=somaidade/4

print(f" A media das idades é igual a  {mediaidade}")
print(f"O homen mais velho tem {maioridadehomen} e seu nome é{nomevelho}")
print(f" Ao todo há {mulhertot20} mulheres com mais de 20 anos")
